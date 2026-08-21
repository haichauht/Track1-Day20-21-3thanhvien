# Run metrics

| Metric | Tutor v1 | Tutor v2 (instrumented) | Tutor v3 (LangSmith verified) |
|---|---:|---:|---:|
| Rows | 24 | 24 | 24 |
| Total tokens | 134.087 | 133.750 | 137.755 |
| Prompt tokens | 125.312 | 125.388 | 128.952 |
| Completion tokens | 8.775 | 8.362 | 8.803 |
| Latency trung bình | 5,55s | 5,09s | 6,26s |
| Latency p95 | 7,52s | 6,83s | 8,96s |
| Cost tổng | $0,024062 | $0,023825 | $0,024625 |
| Cost trung bình/row | $0,001003 | $0,000993 | $0,001026 |
| Rows có tool call | không ghi do bug instrumentation | 24/24 | 24/24 |
| Tool calls | không ghi do bug instrumentation | 39 | 39 |
| Steps trung bình | không ghi do bug instrumentation | 2,04 | 2,08 |

V2 chỉ sửa instrumentation trong `run_eval.py` để lưu `tool_calls`, `steps`,
`finish_reason` và đưa tool evidence vào trace; không đổi tutor prompt/model/retrieval.
V3 là batch xác minh key/permalink LangSmith: 24 tutor traces + 24 judge traces, 0 lỗi.
