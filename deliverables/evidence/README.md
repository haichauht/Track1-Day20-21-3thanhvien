# evidence/ — canonical 30-row artifacts

Thư mục này chỉ giữ artifact hiện hành đã bao phủ đủ 30 scenarios; không lưu các bản
partial, label provisional hoặc placeholder rỗng.

| File | Nội dung |
|---|---|
| `dataset-v1.jsonl` | Dataset canonical sc-01–sc-30 |
| `results-v1.jsonl` | Output tutor thật đủ 30 rows, gồm tool calls, tokens và cost |
| `labels-hai-chau.csv` | Nhãn Hải Châu đủ 30 rows |
| `code-checks-v1-30.txt` | Code checks trên đủ 30 rows |
| `report-v1.html` | Report tổng hợp đủ 30 rows |
| `report-phase2-hai-chau.html` | Report blind Hải Châu đủ 30 rows |
| `report-phase2-yen.html` | Report blind Yến đủ 30 rows |
| `report-phase2-huyen.html` | Report blind Huyền đủ 30 rows |
| `input-candidates-v1.csv` | 30 candidate inputs của Phase 1 |
| `run-metrics.md` | Metrics của canonical 30-row run |
| `braintrust-link.md` | Link tracing và trạng thái canonical |
| `offline-tests.txt` | Kết quả test kỹ thuật |
| `phase2-human-baseline-status.md` | Trạng thái human baseline và việc còn thiếu |

Khi Yến và Huyền hoàn tất nhãn, lưu hai CSV đủ 30 rows tại đây. Sau khi đo agreement
và chốt human gold 30 rows, mới chạy judge canonical và lưu prompt/verdict của lần chạy
đó; không đưa artifact partial trở lại thư mục này.
