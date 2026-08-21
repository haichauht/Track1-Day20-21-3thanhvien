"""So nhãn người của 2–3 thành viên — đo disagreement trước khi đồng thuận.

Mỗi thành viên chấm độc lập trong report.html rồi Export labels.csv, đổi tên thành
labels-<tên>.csv. Sau đó:

    python3 agreement.py labels-an.csv labels-binh.csv labels-chi.csv

In ra: coverage, % đồng thuận hoàn toàn, % từng cặp, case bất đồng kèm note và
tiêu chí gây bất đồng (đem vào thảo luận để chốt nhãn vàng ở Phase 3).
"""
import argparse
from collections import Counter
import csv
from pathlib import Path


VALID_LABELS = {"pass", "fail", "uncertain"}
CATEGORY_TERMS = {
    "answer_grounded": ("ground", "nội dung", "answer", "bám nguồn", "factual"),
    "citation": ("citation", "cite", "quote", "doc", "section", "trích"),
    "followup_quality": ("follow", "gợi mở", "câu hỏi tiếp"),
    "scope": ("scope", "out_of_scope", "in_scope", "ngoài phạm vi", "từ chối"),
    "schema_tool": ("schema", "json", "tool", "kb_search"),
}


def read_labels(path):
    with open(path, encoding="utf-8") as f:
        rows = {}
        for r in csv.DictReader(f):
            sid = r.get("scenario_id", "").strip()
            label = r.get("label", "").strip().lower()
            if not sid or not label:
                continue
            if label not in VALID_LABELS:
                raise SystemExit(f"{path}: {sid} có label không hợp lệ: {label}")
            if sid in rows:
                raise SystemExit(f"{path}: scenario_id bị lặp: {sid}")
            rows[sid] = {"label": label, "note": r.get("note", "").strip()}
        return rows


def note_categories(note):
    text = note.casefold()
    found = [name for name, terms in CATEGORY_TERMS.items()
             if any(term in text for term in terms)]
    return found or (["other"] if text.strip() else ["missing_note"])


def build_report(paths):
    if len(paths) < 2:
        raise SystemExit("Cần ít nhất 2 file: python3 eval/agreement.py labels-a.csv labels-b.csv")
    members = {Path(p).stem.removeprefix("labels-"): read_labels(p) for p in paths}
    common = set.intersection(*[set(m) for m in members.values()])
    if not common:
        raise SystemExit("Không có scenario_id nào chung giữa các file.")

    names = list(members)
    disagree = []
    full_agree = 0
    for sid in sorted(common):
        votes = {n: members[n][sid]["label"] for n in names}
        if len(set(votes.values())) == 1:
            full_agree += 1
        else:
            disagree.append((sid, votes))

    lines = ["Human–human agreement (trước đồng thuận)", ""]
    lines.append("Coverage từng rater: " + " · ".join(
        f"{name}: {len(members[name])}" for name in names))
    lines.append(f"Case chung: {len(common)}")
    lines.append(f"Đồng thuận hoàn toàn: {full_agree}/{len(common)} = {100 * full_agree / len(common):.1f}%")
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = names[i], names[j]
            same = sum(1 for sid in common
                       if members[a][sid]["label"] == members[b][sid]["label"])
            lines.append(f"  {a} vs {b}: {same}/{len(common)} = {100 * same / len(common):.1f}%")

    if disagree:
        lines.append(f"\n{len(disagree)} case bất đồng — đem vào thảo luận:")
        criteria = Counter()
        for sid, votes in disagree:
            lines.append("  " + sid + " -> " + " · ".join(
                f"{n}: {votes[n]} [{members[n][sid]['note'] or 'không có note'}]"
                for n in names))
            for n in names:
                criteria.update(note_categories(members[n][sid]["note"]))
        lines.append("\nTiêu chí xuất hiện trong note của case bất đồng:")
        for criterion, count in criteria.most_common():
            lines.append(f"  {criterion}: {count}")
    else:
        lines.append("\nKhông có case bất đồng trong tập scenario chung.")
    lines.append("\nBước tiếp: thảo luận từng case bất đồng -> chốt nhãn vàng chung vào labels.csv")
    return "\n".join(lines) + "\n"


def main(argv=None):
    parser = argparse.ArgumentParser(description="Đo human–human agreement")
    parser.add_argument("paths", nargs="+", help="2–3 file labels-<tên>.csv")
    parser.add_argument("--output", help="Lưu nguyên báo cáo vào file evidence")
    args = parser.parse_args(argv)
    report = build_report(args.paths)
    print(report, end="")
    if args.output:
        Path(args.output).write_text(report, encoding="utf-8")
        print(f"Đã lưu: {args.output}")


if __name__ == "__main__":
    main()
