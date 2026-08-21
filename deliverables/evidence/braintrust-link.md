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
| `sc-01` | [Mở trace](https://smith.langchain.com/public/7faab492-7a8e-4d71-8858-60710a85b94f/r) |
| `sc-02` | [Mở trace](https://smith.langchain.com/public/b6214ade-51c0-4e8a-81f1-6bbdfb30d3be/r) |
| `sc-03` | [Mở trace](https://smith.langchain.com/public/f5069d21-48b0-4e99-af5e-7945566de77d/r) |
| `sc-04` | [Mở trace](https://smith.langchain.com/public/a18d607b-55f3-4265-aac3-3e624d7dafb1/r) |
| `sc-05` | [Mở trace](https://smith.langchain.com/public/1815d198-0e86-443a-a2b0-00dd451c5457/r) |
| `sc-06` | [Mở trace](https://smith.langchain.com/public/0511a241-eb3e-4dbb-8eb6-0bcc131635e0/r) |
| `sc-07` | [Mở trace](https://smith.langchain.com/public/642657f9-990f-4007-90e3-7c7066e66857/r) |
| `sc-08` | [Mở trace](https://smith.langchain.com/public/684ed398-3bb9-468b-a791-4a6d7b7ac051/r) |
| `sc-09` | [Mở trace](https://smith.langchain.com/public/561dbf44-40eb-42fe-9ec5-642820f1ebbc/r) |
| `sc-10` | [Mở trace](https://smith.langchain.com/public/11448bb8-316f-473b-8dd1-3296b5934740/r) |
| `sc-11` | [Mở trace](https://smith.langchain.com/public/6e3c5e36-7c2d-46dd-afa7-37276210a247/r) |
| `sc-12` | [Mở trace](https://smith.langchain.com/public/5ec03bbd-cd58-40a6-89a6-eacae6398aaf/r) |
| `sc-13` | [Mở trace](https://smith.langchain.com/public/08327529-fca3-4f59-9fbe-e5ce8d9afcb6/r) |
| `sc-14` | [Mở trace](https://smith.langchain.com/public/3c30ad0f-0c72-483d-9996-7c548c41a0d0/r) |
| `sc-15` | [Mở trace](https://smith.langchain.com/public/74ef1d18-9c2a-4f38-9df3-9f7c3b2715c8/r) |
| `sc-16` | [Mở trace](https://smith.langchain.com/public/af6149fc-c25d-4327-a8b5-ef72ce1b8176/r) |
| `sc-17` | [Mở trace](https://smith.langchain.com/public/772e3f30-b0f3-4624-ab2d-dddb532586ec/r) |
| `sc-18` | [Mở trace](https://smith.langchain.com/public/5265de4b-9835-41cf-9f3f-d1bc1b2a8c63/r) |
| `sc-19` | [Mở trace](https://smith.langchain.com/public/987b7646-1839-4030-9993-ede16056c1b7/r) |
| `sc-20` | [Mở trace](https://smith.langchain.com/public/69d9c6f6-d629-426b-958e-0d93713a961a/r) |
| `sc-21` | [Mở trace](https://smith.langchain.com/public/e7702e1f-32a7-4717-bd10-1ed4a9f4a3f4/r) |
| `sc-22` | [Mở trace](https://smith.langchain.com/public/3fc71721-8426-4fb7-bcb2-d8ac1621331f/r) |
| `sc-23` | [Mở trace](https://smith.langchain.com/public/5198e001-0597-4989-a34b-dad5e9a96782/r) |
| `sc-24` | [Mở trace](https://smith.langchain.com/public/25f67d0f-46ad-46ce-aa69-df4eabd1dbd9/r) |
| `sc-25` | [Mở trace](https://smith.langchain.com/public/4bc9aa75-a6f1-4696-89d9-9a5632a3f6a5/r) |
| `sc-26` | [Mở trace](https://smith.langchain.com/public/81155a84-c4e3-4cdb-b81a-3459da942c4a/r) |
| `sc-27` | [Mở trace](https://smith.langchain.com/public/1fa0adc8-1c32-490d-b8e4-b15b5f22fb8b/r) |
| `sc-28` | [Mở trace](https://smith.langchain.com/public/0d73799c-bf84-43a7-a7fb-b3f3d5528e33/r) |
| `sc-29` | [Mở trace](https://smith.langchain.com/public/089cc8df-d531-4792-a17d-c2207843580f/r) |
| `sc-30` | [Mở trace](https://smith.langchain.com/public/461ae477-03ad-4387-9e4a-b4b5055f22cd/r) |

Kết quả local: tutor canonical v1 chạy thành công 30/30. Judge canonical chỉ được chạy
sau khi hoàn tất human gold 30 rows; không dùng các run cũ làm calibration evidence.
