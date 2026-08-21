# evidence/ — data thô của từng bước eval loop

Thư mục này chứa **data thô** minh chứng cho mọi quyết định trong các file
`deliverables/REPORT.md`. File làm việc sinh ra ở **root repo**
(`dataset.jsonl`, `results.jsonl`, `verdicts.jsonl`, `labels.csv`) — chốt một vòng
là copy vào đây ngay, đặt tên theo version, KHÔNG ghi đè vòng cũ.

Cần có đủ:

| File | Lấy từ đâu | Là gì |
|---|---|---|
| `dataset-v1.jsonl` | `dataset.jsonl` (root) | Dataset chính thức 30 rows — đầu vào mọi lần chạy |
| `dataset-v1-addon-traps.jsonl` | 6 rows cuối của v1 | English, teencode, no-referent, mixed-scope, false premise, source bypass |
| `dataset-v1-legacy-24.jsonl` | dataset v1 trước khi mở rộng | Snapshot lịch sử 24 rows, không dùng để chấm vòng mới |
| `results-v1.jsonl` | `results.jsonl` (root) | Output tutor thật đủ 30 rows: input, output JSON, `tool_calls`, tokens, cost từng câu |
| `results-v1-addon-traps.jsonl` | run tutor riêng sc-25–sc-30 | Sáu output mới đã được gộp vào `results-v1.jsonl` |
| `labels.csv` | Export từ `report.html` | Nhãn người của các thành viên (vòng chấm độc lập) |
| `judge-prompt-v1.md` (v2...) | `eval/judge_prompt.md` | Prompt judge TỪNG VÒNG — copy trước mỗi lần sửa |
| `verdicts-v1.jsonl` (sẽ tạo) | `verdicts.jsonl` (root) | Output judge canonical sau khi có human gold 30 rows; hiện chưa chạy |
| `braintrust-link.md` | tự tạo | Link project Braintrust/LangSmith — trace mọi run |

Artifact bổ sung của bài hiện tại:

- `results-legacy24-v1/v2/v3-traced.jsonl` và
  `verdicts-legacy24-v1/v2/v3-traced.jsonl`: lịch sử chạy/calibration của dataset 24
  rows; v3 đã được xác minh trên LangSmith. Các verdict này không phải verdict của
  dataset v1 30 rows hiện tại.
- `input-candidates-v1.csv`: 30 paraphrase AI (2 câu × 15 combinations), chờ người
  nộp điền `human_decision` Keep/Rewrite/Reject và `human_edit` nếu Rewrite.
- `code-checks-v1-30.txt`: code checks hiện hành trên canonical v1; các file
  `code-checks-v1/v2.txt` và `manual-review-v1.csv` là lịch sử legacy24. `run-metrics.md`
  tách rõ hai tập số liệu.
- `labels.csv`: placeholder gold hiện trống; `labels-provisional-ai.csv` chỉ dùng kiểm
  pipeline, không phải human baseline.
- `report-phase2-hai-chau/yen/huyen.html`: ba report blind độc lập, mỗi report đủ 30 rows.
- `report-legacy24.html`: report cũ 24 rows chỉ để audit lịch sử.
- `phase2-human-baseline-status.md`: checklist GATE 2 và trạng thái human-only.

Số liệu trong mục 5 (Calibration Report) của `deliverables/REPORT.md` phải đối chiếu được với các
file ở đây (confusion matrix, % agreement in ra từ `eval/judge.py`).

Nhớ: chạy xong một vòng là copy ngay — cuối buổi mới gom là mất dấu các vòng trước.
