# AI Support Log

> Ghi lại bạn đã dùng AI (ChatGPT/Claude/Kimi...) ở những bước nào khi làm eval-pack.
> Trung thực là một phần của bài nộp — không ai làm một mình, quan trọng là bạn giữ
> quyền kiểm soát chất lượng.

| # | Bước | AI dùng để làm gì | Bạn kiểm chứng kết quả thế nào |
|---|------|-------------------|-------------------------------|
| 1 | Đọc đề và audit repo | Đối chiếu template, liệt kê artifact còn thiếu | So lại từng yêu cầu trong đề gốc và `deliverables/README.md` |
| 2 | Phase 1 | Đề xuất 4 dimensions, 15 combinations và paraphrase 24 inputs | Kiểm tra mỗi row có behavior/risk khác, validate JSONL và coverage bắt buộc |
| 3 | Phase 3 | Soạn nháp rubric blocker/non-blocker và routing | Đối chiếu với output contract, corpus manifest và khả năng kiểm deterministic |
| 4 | Code checks | Mở rộng từ 3 lên 7 checks | Chạy 44 test offline; đọc từng lỗi trên raw result khi có |
| 5 | Phase 4 | Phân tích disagreement, đề xuất prompt judge v2 | Lưu hai prompt/verdict, tính confusion matrix/TPR/TNR từ raw files |
| 6 | Phase 5–6 | Tính slice, soạn scorecard và verdict draft | Đối chiếu `results-v*`, code checks và manual review; giữ nguyên gate chốt trước |
| 7 | Instrumentation | Phát hiện thiếu tool_calls và tracing báo thành công giả | Sửa runner/tracer, tạo results-v2; thay key, xác thực LangSmith và kiểm đủ 48 trace không lỗi |
| 8 | Đồng bộ repo | Map bài từ starter cũ sang cấu trúc `tutor/`, `eval/`, `tests/`, `deliverables/` | So cùng merge-base, giữ template mới, chạy lại test và audit file/key trước push |

- Phần nào AI gợi ý mà bạn **bác bỏ**? Vì sao?
  - Bác bỏ việc coi nhiều paraphrase cùng intent là coverage mới.
  - Bác bỏ việc dùng overall pass rate làm gate nếu critical slice còn fail.
  - Bác bỏ việc gọi nhãn do AI tạo là “nhãn người” hoặc “đồng thuận ba thành viên”.
- Phần nào bạn **hoàn toàn tự làm**?
  - Người nộp phải tự xác nhận dimensions/combinations, gán nhãn Phase 2, bảo vệ
    threshold, verdict và reflection. Bản hiện tại ghi rõ phần AI hỗ trợ thay vì giả
    mạo quyết định/nhãn của con người.
