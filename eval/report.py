"""Sinh report HTML TĨNH (mở bằng double-click, không cần server/mạng).

Đọc results.jsonl + verdicts.jsonl + labels.csv, nhúng toàn bộ dữ liệu vào HTML.
Nhãn pass/fail/uncertain bấm trong report được lưu vào localStorage của trình duyệt;
nút "Export labels.csv" tải về file CSV để đưa lại cho judge.py so agreement.

Phase 2 phải chấm mù, không nhìn judge/nhãn AI:
  python eval/report.py --blind --rater hai-chau
Lệnh này sinh report-phase2-hai-chau.html, dùng vùng lưu riêng và export
labels-hai-chau.csv có cả cột note.
"""
import argparse, csv, json, os, re

def read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]

def read_labels(path="labels.csv"):
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return {r["scenario_id"]: {
                    "label": r.get("label", "").strip(),
                    "note": r.get("note", "").strip(),
                }
                for r in csv.DictReader(f) if r.get("scenario_id")}

def _safe_name(value):
    value = re.sub(r"[^a-zA-Z0-9_-]+", "-", value.strip()).strip("-")
    return value or "rater"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Sinh report review cho eval results")
    parser.add_argument("--blind", action="store_true",
                        help="Ẩn judge và nhãn cũ để chấm human baseline độc lập")
    parser.add_argument("--rater", default="rater",
                        help="Tên ngắn dùng cho localStorage và file labels export")
    parser.add_argument("--output", help="Tên file HTML đầu ra")
    args = parser.parse_args(argv)
    rater = _safe_name(args.rater)

    results = read_jsonl("results.jsonl")
    verdicts = ({v["scenario_id"]: v for v in read_jsonl("verdicts.jsonl")}
                if not args.blind else {})
    labels = read_labels() if not args.blind else {}
    if not results:
        print("Chưa có results.jsonl — report sẽ trống. Chạy python3 run_eval.py trước.")
    # Gộp 3 nguồn thành 1 list row để nhúng vào HTML
    rows = []
    for r in results:
        sid = r.get("scenario_id", "?")
        prior = labels.get(sid, {})
        rows.append({"scenario_id": sid, "input": r.get("input", ""),
                     "slide": r.get("slide"),
                     "expected_scope": r.get("expected_scope"),
                     "metadata": r.get("metadata") or {},
                     "output": r.get("output"), "error": r.get("error"),
                     "raw_content": r.get("raw_content", ""),
                     "latency_s": r.get("latency_s"), "cost_usd": r.get("cost_usd"),
                     "verdict": verdicts.get(sid, {}).get("verdict"),
                     "rationale": verdicts.get(sid, {}).get("rationale", ""),
                     "show_judge": not args.blind,
                     "human_label": prior.get("label", ""),
                     "human_note": prior.get("note", "")})
    output = args.output or (f"report-phase2-{rater}.html" if args.blind else "report.html")
    export_name = f"labels-{rater}.csv" if args.blind else "labels.csv"
    storage_key = f"evalkit-phase2-{rater}" if args.blind else "evalkit-labels"
    mode = (f"Blind human review · rater: {rater} · judge/nhãn cũ đã ẩn"
            if args.blind else "Review tổng hợp")
    html = (TEMPLATE.replace("__DATA__", json.dumps(rows, ensure_ascii=False))
                    .replace("__STORAGE_KEY__", json.dumps(storage_key))
                    .replace("__EXPORT_NAME__", json.dumps(export_name))
                    .replace("__MODE__", mode))
    with open(output, "w", encoding="utf-8") as f:
        f.write(html)
    print("Đã sinh %s (%d dòng dữ liệu)." % (output, len(rows)))
    if args.blind:
        print("Chế độ blind: không nhúng verdict/rationale của judge hoặc nhãn cũ.")
        print("Khi chấm xong, bấm Export -> %s" % export_name)

# Giao diện: mọi logic render/lọc/gán nhãn chạy hoàn toàn trong trình duyệt.
TEMPLATE = """<!doctype html><html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Eval report — AI Tutor</title><style>
body{font-family:-apple-system,system-ui,sans-serif;margin:0;background:#f6f7f9;color:#222}
header{position:sticky;top:0;background:#fff;border-bottom:1px solid #e2e4e8;padding:10px 16px;display:flex;gap:10px;flex-wrap:wrap;align-items:center;z-index:9}
h1{font-size:16px;margin:0 12px 0 0}
select,button{font-size:13px;padding:5px 10px;border:1px solid #ccd;border-radius:6px;background:#fff;cursor:pointer}
main{max-width:960px;margin:16px auto;padding:0 12px}
.card{background:#fff;border:1px solid #e2e4e8;border-radius:10px;padding:14px;margin-bottom:14px}
.q{font-weight:600;margin-bottom:8px}
.meta{font-size:12px;color:#778;margin-bottom:8px}
.badge{display:inline-block;padding:2px 8px;border-radius:10px;font-size:12px;font-weight:600}
.pass{background:#e3f5e9;color:#176b36}.fail{background:#fde8e8;color:#a32727}.uncertain{background:#fdf3dc;color:#8a6100}
.src{font-size:13px;background:#f4f6f8;border-left:3px solid #9db4c8;padding:6px 10px;margin:6px 0;border-radius:0 6px 6px 0}
.src code{color:#356}
.fu{margin:4px 0 4px 18px;font-size:14px}
.raw{display:none;white-space:pre-wrap;background:#1d1f24;color:#d6dce4;font-size:12px;padding:10px;border-radius:8px;overflow:auto;max-height:320px}
.lbl button.on{background:#223;color:#fff;border-color:#223}
.rat{font-size:13px;color:#555;margin-top:6px}
.mode{font-size:12px;color:#704f00;background:#fff3cd;padding:3px 8px;border-radius:8px}
.note{width:100%;box-sizing:border-box;margin-top:7px;padding:7px 9px;border:1px solid #ccd;border-radius:6px;font-size:13px}
</style></head><body>
<header><h1>Eval report — AI Tutor</h1>
Lọc verdict: <select id="flt"><option value="">Tất cả</option><option>pass</option><option>fail</option><option>uncertain</option><option value="none">(chưa chấm)</option></select>
<span class="mode">__MODE__</span>
<button onclick="exportCsv()">Export CSV</button><button onclick="resetReview()">Xoá nhãn trên máy</button><span id="stat"></span></header>
<main id="list"></main>
<script>
var ROWS=__DATA__, KEY=__STORAGE_KEY__, EXPORT_NAME=__EXPORT_NAME__;
var saved={};try{saved=JSON.parse(localStorage.getItem(KEY)||"{}")}catch(e){}
function esc(s){return String(s==null?"":s).replace(/[&<>"]/g,function(c){return{"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]})}
function badge(v){return v?'<span class="badge '+v+'">judge: '+v+'</span>':'<span class="badge">chưa chấm</span>'}
function state(r){var x=saved[r.scenario_id];if(typeof x=="string")x={label:x,note:""};return x||{label:r.human_label||"",note:r.human_note||""}}
function persist(){localStorage.setItem(KEY,JSON.stringify(saved))}
function render(){
 var f=document.getElementById("flt").value,el=document.getElementById("list"),h="",n=0;
 ROWS.forEach(function(r,i){
  if(f&&((f=="none"&&r.verdict)||(f!="none"&&r.verdict!=f)))return;n++;
  var o=r.output||{},st=state(r),lbl=st.label||"";
  h+='<div class="card"><div class="meta">'+esc(r.scenario_id)+' &middot; '+esc(o.scope||"")+
  (r.latency_s!=null?' &middot; '+r.latency_s+'s':'')+(r.cost_usd!=null?' &middot; ~$'+r.cost_usd:'')+'</div>';
  if(r.slide)h+='<div class="meta" style="color:#346">Đang xem slide '+esc(r.slide.id)+' — '+esc(r.slide.title)+(r.slide.keyword?' &middot; từ khoá: <b>'+esc(r.slide.keyword)+'</b>':'')+'</div>';
  h+='<div class="q">'+esc(r.input)+'</div>';
  if(r.error)h+='<div class="badge fail">lỗi chạy</div><div class="rat">'+esc(r.error)+'</div>';
  else{h+='<div>'+esc(o.answer||"(không parse được answer)")+'</div>';
   (o.sources||[]).forEach(function(s){h+='<div class="src"><code>'+esc(s.doc_id)+'#'+esc(s.section_id)+'</code> — “'+esc(s.quote)+'”</div>'});
   if(o.followup_questions)h+='<div style="margin-top:6px"><b>Gợi ý hỏi tiếp:</b></div>'+o.followup_questions.map(function(q){return '<div class="fu">• '+esc(q)+'</div>'}).join("");}
  if(r.show_judge)h+='<div style="margin-top:10px">'+badge(r.verdict)+' <span class="rat">'+esc(r.rationale)+'</span></div>';
  h+=
  '<div class="lbl" style="margin-top:8px">Nhãn người: '+["pass","fail","uncertain"].map(function(v){
   return '<button data-i="'+i+'" data-v="'+v+'" class="'+(lbl==v?"on":"")+'" onclick="setLabel(this)">'+v+'</button>'}).join(" ")+
  ' <button data-i="'+i+'" onclick="raw(this)">xem raw</button></div>'+
  '<input class="note" data-i="'+i+'" value="'+esc(st.note||"")+'" oninput="setNote(this)" placeholder="Note khi fail/uncertain, ví dụ: fail: citation — quote không khớp section">'+
  '<div class="raw">'+esc(r.raw_content||JSON.stringify(o,null,2))+'</div></div>';});
 el.innerHTML=h||"<p>Không có dòng nào khớp bộ lọc.</p>";
 var done=ROWS.filter(function(r){return !!state(r).label}).length;
 document.getElementById("stat").textContent=done+"/"+ROWS.length+" đã chấm · "+n+" đang hiện";}
function setLabel(b){var r=ROWS[b.dataset.i];
 var st=state(r);st.label=st.label==b.dataset.v?"":b.dataset.v;saved[r.scenario_id]=st;
 persist();render();}
function setNote(b){var r=ROWS[b.dataset.i],st=state(r);st.note=b.value;saved[r.scenario_id]=st;persist()}
function raw(b){var d=b.closest(".card").querySelector(".raw");d.style.display=d.style.display=="block"?"none":"block";}
function csv(v){return '"'+String(v==null?"":v).replace(/"/g,'""')+'"'}
function exportCsv(){var s="scenario_id,label,note\\n";
 ROWS.forEach(function(r){var st=state(r);s+=csv(r.scenario_id)+","+csv(st.label)+","+csv(st.note)+"\\n"});
 var a=document.createElement("a");a.href=URL.createObjectURL(new Blob([s],{type:"text/csv"}));
 a.download=EXPORT_NAME;a.click();}
function resetReview(){if(confirm("Xoá toàn bộ nhãn và note đang lưu cho rater này?")){saved={};localStorage.removeItem(KEY);render()}}
document.getElementById("flt").onchange=render;render();
</script></body></html>"""

if __name__ == "__main__":
    main()
