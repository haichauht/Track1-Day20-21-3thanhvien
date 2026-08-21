# AI Support Log — Huỳnh Thị Hải Châu · 2A202601912

AI được dùng để brainstorm, kiểm tra và soạn nháp; quyền chọn coverage, nhãn người và
quyết định release vẫn thuộc con người.

| Bước | AI đã giúp tôi ở đâu? | Tôi kiểm chứng thế nào? |
|---|---|---|
| Phase 1 | Gợi ý dimension/value và paraphrase input synthetic sau khi nhóm khóa coverage | Tôi kiểm từng row có behavior/risk khác thật, loại biến chỉ làm đổi cách viết và giữ nhãn `synthetic-reviewed` |
| Phase 1–2 | Tóm tắt phân bố 30 rows theo scope, set type, clarity và coverage | Tôi đếm lại từ `dataset-v1.jsonl` và đọc đủ 30 input/output trước khi gán nhãn |
| Phase 4 | Gợi ý assertion cho schema, citation, quote và tool contract | Tôi chạy code trên 30 rows, đối chiếu citation fail với corpus và không cho LLM đảo kết quả deterministic |
| Phase 5 | Gom danh sách quote fail và so candidate v2/v3 | Tôi kiểm `code-checks-v3.txt`, raw JSONL và row IDs trước khi đưa số vào scorecard |
| Evidence | Soạn bảng artifact và kiểm tra liên kết | Tôi chỉ giữ file chạy thật có version; file scratch/error ở root không được dùng làm evidence |

## AI sai, hồi hộp hoặc làm mất coverage ở đâu?

- Một gợi ý coi persona là dimension quyết định behavior; tôi loại vì persona chủ yếu
  làm câu tự nhiên, còn coverage/scope/clarity mới đổi đáp án đúng.
- AI có lúc coi “citation tồn tại” là đủ pass dù quote dịch hoặc dùng `...`; tôi giữ
  rule span nguyên văn liên tiếp và để 11 rows v3 fail code gate.
- Khi audit v3, AI từng yêu cầu `tool_calls` không rỗng ở mọi row. Tôi sửa lại:
  out-of-scope có thể không search; câu in-scope mới bắt buộc qua tool contract.
- AI không được phép suy ra production coverage từ 30 câu synthetic; hạn chế này được
  giữ nguyên trong REPORT.

## Tôi đã tự sửa hoặc quyết định lại điều gì?

- Chốt bốn dimension của Input Grid và giữ risk thành slice riêng.
- Chấm độc lập 30 rows, giữ phiếu `sc-30` của mình trong disagreement evidence.
- Giao các kiểm tra có referent tuyệt đối cho code và chạy code trước judge.
- Xác nhận candidate v3 **HOLD** dù operational gate xanh, vì quote quality gate fail.
