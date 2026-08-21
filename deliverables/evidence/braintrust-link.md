# Tracing evidence — LangSmith

- Backend: LangSmith.
- Project: `ai-evaluation`.
- Model tutor: `openai/gpt-4o-mini`.
- Model judge: `openai/gpt-4o`.
- Tutor/judge gọi trực tiếp `api.openai.com`; không dùng custom gateway.
- Ngày xác minh: 2026-08-21.
- Kết quả xác minh qua LangSmith API: key hợp lệ, project tồn tại, có 48 root traces mới
  trong batch cuối (24 `tutor-run` + 24 `judge-run`), 0 trace lỗi.

**Permalink project:**
https://smith.langchain.com/o/f4c97ae7-958f-49d7-a7d6-b1e3fdef3b55/projects/p/5aa21963-14bd-44a9-ad20-576581db4336

Kết quả local của batch cuối: tutor 24/24 thành công; judge 24/24 thành công;
agreement với bộ nhãn provisional dùng tại thời điểm chạy là 17/24 (71%). File
`labels.csv` hiện để trống để chờ human gold thật; không dùng 71% như human agreement.
