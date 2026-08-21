# Run metrics

| Metric | Legacy v1 | Legacy v2 (instrumented) | Legacy v3 (traced) | Canonical v1 (30 rows) |
|---|---:|---:|---:|---:|
| Rows | 24 | 24 | 24 | 30 |
| Total tokens | 134.087 | 133.750 | 137.755 | 174.344 |
| Prompt tokens | 125.312 | 125.388 | 128.952 | 163.750 |
| Completion tokens | 8.775 | 8.362 | 8.803 | 10.594 |
| Latency trung bình | 5,55s | 5,09s | 6,26s | 6,53s |
| Latency p95 | 7,52s | 6,83s | 8,96s | 9,23s |
| Cost tổng | $0,024062 | $0,023825 | $0,024625 | $0,030919 |
| Cost trung bình/row | $0,001003 | $0,000993 | $0,001026 | $0,001031 |
| Rows có tool call | không ghi do bug instrumentation | 24/24 | 24/24 | 30/30 |
| Tool calls | không ghi do bug instrumentation | 39 | 39 | 46 |
| Steps trung bình | không ghi do bug instrumentation | 2,04 | 2,08 | 2,07 |

Legacy v2 chỉ sửa instrumentation trong `run_eval.py` để lưu `tool_calls`, `steps`,
`finish_reason` và đưa tool evidence vào trace; không đổi tutor prompt/model/retrieval.
Legacy v3 là batch xác minh key/permalink LangSmith: 24 tutor traces + 24 judge traces,
0 lỗi. Canonical v1 ghép output legacy v3 với run traced riêng của sáu trap mới; cả
30 rows đều dùng cùng tutor/model/prompt và không có lỗi chạy.
