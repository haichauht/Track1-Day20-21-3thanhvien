# Tracing evidence — LangSmith

- Backend: LangSmith.
- Project: `ai-evaluation`.
- Model tutor: `openai/gpt-4o-mini`.
- Model judge: `openai/gpt-4o`.
- Tutor/judge gọi trực tiếp `api.openai.com`; không dùng custom gateway.
- Ngày xác minh: 2026-08-21.
- Kết quả canonical: đủ 30 `tutor-run` cho `sc-01`–`sc-30`, không có trace lỗi.

## Project permalink

[Mở project `ai-evaluation` trên LangSmith](https://smith.langchain.com/o/f4c97ae7-958f-49d7-a7d6-b1e3fdef3b55/projects/p/5aa21963-14bd-44a9-ad20-576581db4336)

Project permalink yêu cầu đăng nhập và có quyền truy cập workspace. Người chấm không có tài khoản
hoặc chưa được mời vào workspace có thể dùng các public trace bên dưới.

## Public trace index — canonical tutor v1

Các link sau mở được mà không cần đăng nhập và bao phủ đủ batch canonical `sc-01`–`sc-30`.

| Scenario | Public trace |
|---|---|
| `sc-01` | [Mở trace](https://smith.langchain.com/public/4bf38883-e608-4fa1-a11c-ee3fd19b2e26/r) |
| `sc-02` | [Mở trace](https://smith.langchain.com/public/a9e4d363-346c-498c-bbff-2330fca352b2/r) |
| `sc-03` | [Mở trace](https://smith.langchain.com/public/74c60f3e-333e-43a5-a921-cae52cffeb42/r) |
| `sc-04` | [Mở trace](https://smith.langchain.com/public/b6486f82-d98f-4022-b2a3-2f070c94cf2a/r) |
| `sc-05` | [Mở trace](https://smith.langchain.com/public/c0403820-71e7-42a2-97a1-3ea758b422a4/r) |
| `sc-06` | [Mở trace](https://smith.langchain.com/public/76f030a8-bf88-4baa-8d1d-f107416cde20/r) |
| `sc-07` | [Mở trace](https://smith.langchain.com/public/5c706c1d-af12-4bb3-9130-d5c157e0b431/r) |
| `sc-08` | [Mở trace](https://smith.langchain.com/public/ac00e53a-33df-4f42-b4f9-992e1851c835/r) |
| `sc-09` | [Mở trace](https://smith.langchain.com/public/463eb0f4-de7f-45e4-9573-b57961148297/r) |
| `sc-10` | [Mở trace](https://smith.langchain.com/public/669d39fc-2e98-4e44-b404-e05ef8b534c9/r) |
| `sc-11` | [Mở trace](https://smith.langchain.com/public/91dc3579-8eb9-420b-9cda-47dc1cc3f1d6/r) |
| `sc-12` | [Mở trace](https://smith.langchain.com/public/6d7dc2e8-e8ff-45f9-93f6-08695e1b7f15/r) |
| `sc-13` | [Mở trace](https://smith.langchain.com/public/e78af0ae-3bfb-4b19-a40d-47c789b10a3d/r) |
| `sc-14` | [Mở trace](https://smith.langchain.com/public/d4a35e9c-d1ac-4829-bb46-80852aa112c8/r) |
| `sc-15` | [Mở trace](https://smith.langchain.com/public/2f694249-4361-4e25-9af0-581879c139a7/r) |
| `sc-16` | [Mở trace](https://smith.langchain.com/public/65a4ad07-8a94-45b8-8c8e-153180eaef60/r) |
| `sc-17` | [Mở trace](https://smith.langchain.com/public/4bd408f1-547a-46b6-a7eb-383b26712173/r) |
| `sc-18` | [Mở trace](https://smith.langchain.com/public/1608aff7-fe69-41ab-bcb2-a6df60042d94/r) |
| `sc-19` | [Mở trace](https://smith.langchain.com/public/d301d908-c7b2-4a42-ae4d-1c99edda054f/r) |
| `sc-20` | [Mở trace](https://smith.langchain.com/public/6d492061-b781-489d-81d6-21ec8f4fdb33/r) |
| `sc-21` | [Mở trace](https://smith.langchain.com/public/4dc4e44f-9718-435b-b310-c4e406715c8a/r) |
| `sc-22` | [Mở trace](https://smith.langchain.com/public/559fea19-513f-450a-b687-75a78496ec0c/r) |
| `sc-23` | [Mở trace](https://smith.langchain.com/public/cacb46f0-88c3-4382-bc1b-317104df3223/r) |
| `sc-24` | [Mở trace](https://smith.langchain.com/public/f5cd549a-0524-45c7-a9cd-48121b567ec9/r) |
| `sc-25` | [Mở trace](https://smith.langchain.com/public/708b819f-8f50-4094-872f-476585291afd/r) |
| `sc-26` | [Mở trace](https://smith.langchain.com/public/050101c3-5e87-4b64-9f6a-3f8e3aa701a6/r) |
| `sc-27` | [Mở trace](https://smith.langchain.com/public/2d31c706-1860-4a2c-8da1-fcece24fbc1b/r) |
| `sc-28` | [Mở trace](https://smith.langchain.com/public/f859e117-d5f1-4451-845e-bb18d2e9e887/r) |
| `sc-29` | [Mở trace](https://smith.langchain.com/public/2e7424b1-92d3-44fd-84c9-750fd153658d/r) |
| `sc-30` | [Mở trace](https://smith.langchain.com/public/6c501795-9395-4308-80e2-cbcd46bc4d0a/r) |

Kết quả local: tutor canonical v1 chạy thành công 30/30. Judge canonical chỉ được chạy
sau khi hoàn tất human gold 30 rows; không dùng các run cũ làm calibration evidence.
