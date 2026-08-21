# Tracing evidence — LangSmith

- Backend: LangSmith.
- Project: `ai-evaluation`.
- Model tutor: `openai/gpt-4o-mini`.
- Model judge: `openai/gpt-4o`.
- Tutor/judge gọi trực tiếp `api.openai.com`; không dùng custom gateway.
- Ngày xác minh: 2026-08-21.
- Kết quả xác minh qua LangSmith API và run log: key hợp lệ, project tồn tại, có 54
  root traces được ghi nhận cho evidence hiện tại (30 `tutor-run` + 24 `judge-run`),
  0 trace lỗi. Sáu tutor trace mới là sc-25–sc-30.

**Permalink project:**
https://smith.langchain.com/o/f4c97ae7-958f-49d7-a7d6-b1e3fdef3b55/projects/p/5aa21963-14bd-44a9-ad20-576581db4336

Kết quả local: tutor canonical v1 30/30 thành công; judge legacy24 24/24 thành công;
agreement 17/24 (71%) chỉ là với bộ nhãn provisional legacy dùng tại thời điểm chạy. File
`labels.csv` hiện để trống để chờ human gold thật; không dùng 71% như human agreement.
