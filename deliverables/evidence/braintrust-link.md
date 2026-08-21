# Tracing evidence — LangSmith

- Backend: LangSmith.
- Project: `ai-evaluation`.
- Model tutor: `openai/gpt-4o-mini`.
- Model judge: `openai/gpt-4o`.
- Tutor/judge gọi trực tiếp `api.openai.com`; không dùng custom gateway.
- Ngày xác minh: 2026-08-21.
- Kết quả canonical: đủ 30 `tutor-run` cho sc-01–sc-30, không có trace lỗi.

**Permalink project:**
https://smith.langchain.com/o/f4c97ae7-958f-49d7-a7d6-b1e3fdef3b55/projects/p/5aa21963-14bd-44a9-ad20-576581db4336

Kết quả local: tutor canonical v1 chạy thành công 30/30. Judge canonical chỉ được chạy
sau khi hoàn tất human gold 30 rows; không dùng các run cũ làm calibration evidence.
