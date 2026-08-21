# Eval Pack — quy cách bài nộp capstone AI Evaluation (Day 20–21)

"Chiếc hộp" chứa toàn bộ minh chứng eval loop của nhóm cho VLearn AI Tutor.

**Nguyên tắc bắt buộc:** mỗi bước của eval loop phải nộp đủ ba thứ —
**đầu vào** (bạn cho gì vào), **đầu ra** (hệ thống trả gì ra — file data thô),
và **quyết định** (bạn kết luận/lựa chọn gì ở bước đó, VÌ SAO). Thiếu một trong ba,
bước đó coi như chưa làm.

## Cấu trúc repo nộp (tên thư mục/file cố định)

```text
Track1_Day21_MHV_HoVaTen/
├── README.md                  # thông tin cá nhân + nhóm, đóng góp của tôi, verdict tóm tắt
├── deliverables/              # bài nộp report A→Z + DATA THÔ
│   ├── REPORT.md                  # 7 mục QUYẾT ĐỊNH theo phase (1 Input Grid … 7 Verdict) — viết bằng ngôn ngữ PM
│   └── evidence/                  # DATA THÔ — input/output thật của từng bước chạy
│       ├── dataset-v1.jsonl       # dataset nhóm chốt (đầu vào mọi lần chạy)
│       ├── results-v1.jsonl       # output tutor (mỗi row: input, output JSON, tool_calls, tokens, cost)
│       ├── labels-hai-chau.csv    # nhãn Hải Châu đủ 30 rows
│       ├── labels-yen.csv         # tạo khi Yến chấm đủ 30 rows
│       ├── labels-huyen.csv       # tạo khi Huyền chấm đủ 30 rows
│       ├── labels-gold-v1.csv     # tạo sau agreement, đủ 30 rows
│       ├── judge-prompt-v1-30.md  # tạo khi chạy judge canonical đủ 30 rows
│       ├── verdicts-v1-30.jsonl   # output judge canonical đủ 30 rows
│       └── braintrust-link.md     # link project Braintrust/LangSmith — trace mọi run
└── ai-support-log.md          # bạn dùng AI ở đâu, AI sai ở đâu, bạn quyết lại gì
```

Quy ước phiên bản: mỗi artifact lưu vào evidence phải đủ 30 rows. Mỗi lần chạy lại là
một version mới — `results-v2-30.jsonl`, `verdicts-v2-30.jsonl`... Không đưa snapshot
partial vào thư mục nộp.

## Checklist trước khi nộp

- [ ] `deliverables/REPORT.md` đủ 7 mục (1 Input Grid … 7 Verdict); mục nào cũng có phần **quyết định + vì sao**
- [ ] `deliverables/evidence/` có đủ data thô của mọi bước: dataset, results, labels, judge prompts
      từng vòng, verdicts từng vòng, link Braintrust/LangSmith (trace mọi run)
- [ ] Số liệu trong REPORT.md khớp với data trong deliverables/evidence/ (kiểm chứng được)
- [ ] Verdict có đủ 5 phần report và một quyết định rõ ràng
- [ ] `ai-support-log.md` là của chính người nộp

## Gợi ý

- Mỗi mục trong `deliverables/REPORT.md` đã có sẵn khung câu hỏi dẫn — trả lời ngắn, dẫn chứng
  bằng số/file thật trong `evidence/`, đừng viết chung chung.
- Chạy xong một vòng là copy file ngay vào `evidence/` — để cuối buổi mới gom là mất.
