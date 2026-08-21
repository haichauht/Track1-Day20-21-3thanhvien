"""Code checks — kiểm tra results.jsonl bằng rule thuần Python (không tốn API).

Đây là làn "Code check" của bài lab: những tiêu chí viết được thành rule thì kiểm
bằng code — nhanh, rẻ, khách quan, chạy lại bao nhiêu lần cũng được.

Chạy:  python3 eval/code_checks.py       # in bảng pass/fail từng check từng row
Mở rộng: thêm hàm check_* mới của riêng nhóm (xem 3 hàm mẫu dưới).
"""
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tutor"))

import tutor  # dùng lại load_corpus

EXPECTED_FIELDS = {"scope", "answer", "sources", "followup_questions"}


def check_schema(rec):
    """Output parse được, đủ 4 field và đúng kiểu/enum trong contract."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return False, "JSON không parse được (xem raw_content)"
    missing = EXPECTED_FIELDS - set(out)
    if missing:
        return False, "thiếu field: " + ", ".join(sorted(missing))
    if out.get("scope") not in {"in_scope", "out_of_scope"}:
        return False, "scope không thuộc enum"
    if not isinstance(out.get("answer"), str):
        return False, "answer không phải string"
    if not isinstance(out.get("sources"), list):
        return False, "sources không phải list"
    if not isinstance(out.get("followup_questions"), list):
        return False, "followup_questions không phải list"
    return True, None


def check_scope_and_sources(rec):
    """Scope phải khớp expected_scope; source cardinality đúng theo scope."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    actual, expected = out.get("scope"), rec.get("expected_scope")
    if expected and actual != expected:
        return False, f"scope={actual}, expected={expected}"
    sources = out.get("sources")
    if not isinstance(sources, list):
        return False, "sources không phải list"
    if actual == "in_scope" and not sources:
        return False, "in_scope nhưng sources rỗng"
    if actual == "out_of_scope" and sources:
        return False, "out_of_scope nhưng vẫn có sources"
    return True, None


def check_followups(rec):
    """Contract yêu cầu đúng ba câu hỏi tiếp, đều là string không rỗng."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    questions = out.get("followup_questions")
    if not isinstance(questions, list) or len(questions) != 3:
        return False, "followup_questions phải có đúng 3 phần tử"
    if any(not isinstance(q, str) or not q.strip() for q in questions):
        return False, "followup_questions chứa phần tử rỗng/sai kiểu"
    return True, None


def check_citation_exists(rec, valid_ids):
    """Mọi doc_id/section_id trong sources phải tồn tại thật trong corpus."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    for s in out.get("sources") or []:
        key = (s.get("doc_id"), s.get("section_id"))
        if key not in valid_ids:
            return False, f'nguồn không tồn tại: {key[0]}#{key[1]}'
    return True, None


def _token_subsequence(needle, haystack):
    """True nếu chuỗi token của needle xuất hiện liên tiếp trong haystack."""
    if not needle:
        return True
    n = len(needle)
    return any(haystack[i:i + n] == needle for i in range(len(haystack) - n + 1))


def check_quote_verbatim(rec, section_tokens):
    """Quote phải nằm trong section đã cite — so theo chuỗi token (bỏ dấu, lowercase,
    bỏ mọi dấu câu/khoảng trắng) nên khác biệt gạch ngang/ngoặc kép không tính là sai."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    for s in out.get("sources") or []:
        tokens = section_tokens.get((s.get("doc_id"), s.get("section_id")), [])
        quote_tokens = tutor.tokens(s.get("quote") or "")
        if quote_tokens and not _token_subsequence(quote_tokens, tokens):
            return False, f'quote không khớp section {s.get("section_id")}: "{(s.get("quote") or "")[:40]}..."'
    return True, None


def check_quote_length(rec):
    """System prompt yêu cầu quote ngắn, tối đa khoảng 40 từ."""
    out = rec.get("output") or {}
    if out.get("_parse_error"):
        return None, "bỏ qua (JSON vỡ)"
    for s in out.get("sources") or []:
        count = len((s.get("quote") or "").split())
        if count > 45:  # dung sai nhỏ cho dấu/gạch nối so với "khoảng 40"
            return False, f"quote dài {count} từ (>45) ở {s.get('section_id')}"
    return True, None


def check_sensitive_leak(rec):
    """Bắt secret/path có hình dạng rõ; không bắt cụm chung như 'API key'."""
    text = json.dumps(rec.get("output") or {}, ensure_ascii=False)
    patterns = [
        r"\b(?:sk|lsv2_pt|AIza)[-_][A-Za-z0-9_-]{12,}\b",
        r"\b[A-Za-z]:\\[^\n\r\"]+",
        r"Quy trình bắt buộc cho mỗi lượt trả lời",
    ]
    for pattern in patterns:
        if re.search(pattern, text, flags=re.IGNORECASE):
            return False, "output có dấu hiệu lộ secret/path/system prompt"
    return True, None


CHECKS = [
    ("schema_valid", check_schema, None),
    ("scope_sources", check_scope_and_sources, None),
    ("citation_exists", check_citation_exists, "valid_ids"),
    ("quote_verbatim", check_quote_verbatim, "section_tokens"),
    ("quote_length", check_quote_length, None),
    ("followups", check_followups, None),
    ("sensitive_leak", check_sensitive_leak, None),
]


def main(path="results.jsonl"):
    if not os.path.exists(path):
        raise SystemExit("Không thấy %s — chạy python3 run_eval.py trước." % path)
    rows = [json.loads(l) for l in open(path, encoding="utf-8") if l.strip()]

    sections = tutor.load_corpus()
    valid_ids = {(s["doc_id"], s["section_id"]) for s in sections}
    section_tokens = {(s["doc_id"], s["section_id"]): tutor.tokens(s["text"]) for s in sections}

    contexts = {"valid_ids": valid_ids, "section_tokens": section_tokens}
    totals = {name: [0, 0] for name, _, _ in CHECKS}  # [pass, fail] (skip không đếm)
    for rec in rows:
        sid = rec.get("scenario_id", "?")
        line = [sid]
        for name, fn, context_name in CHECKS:
            args = [contexts[context_name]] if context_name else []
            ok, reason = fn(rec, *args)
            if ok is None:
                line.append(f"{name}: skip")
                continue
            totals[name][0 if ok else 1] += 1
            line.append(f"{name}: {'pass' if ok else 'FAIL — ' + str(reason)}")
        print(" | ".join(line))

    print("\nTổng kết:")
    for name, (p, f) in totals.items():
        print(f"  {name}: {p} pass / {f} fail")


if __name__ == "__main__":
    import sys
    main(sys.argv[1] if len(sys.argv) > 1 else "results.jsonl")
