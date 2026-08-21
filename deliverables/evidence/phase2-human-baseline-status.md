# Phase 2 — Human baseline status

## Phần kỹ thuật đã hoàn tất

- Dataset v1 chính thức có 30 scenarios và `scenario_id` duy nhất.
- Tutor đã chạy thật đủ 30/30; kết quả canonical nằm ở `results-v1.jsonl`.
- LangSmith đã ghi nhận đủ 30 tutor traces, không có trace lỗi. Judge canonical 30
  rows chưa chạy và chỉ được calibrate sau khi có human gold.
- Ba report chấm mù đã sinh: `report-phase2-hai-chau.html`, `report-phase2-yen.html`
  và `report-phase2-huyen.html`.
- Chế độ blind không nhúng verdict/rationale của judge, không nhúng nhãn AI cũ và dùng
  localStorage riêng theo rater.
- UI có đủ `pass` / `fail` / `uncertain` và ô `note`; file export mang tên rater.
- `labels-hai-chau.csv` đã đủ 30/30 rows.
- `agreement.py` đã hỗ trợ coverage, agreement tổng, từng cặp, case bất đồng kèm note
  và thống kê tiêu chí xuất hiện trong note.

## Việc bắt buộc người thật thực hiện

1. Hai thành viên còn lại mở đúng report mang tên mình trong `deliverables/evidence/`:

   - Yến: `report-phase2-yen.html`
   - Huyền: `report-phase2-huyen.html`

2. Mỗi người chấm độc lập đủ 30 scenarios, không xem
   file của nhau. Row là `fail` nếu bất kỳ tiêu chí nào fail. Khi `fail`/`uncertain`, note
   ghi rõ tiêu chí: `answer_grounded`, `citation`, `followup_quality`, `scope` hoặc
   `schema_tool`, kèm lý do ngắn.
3. Mỗi người bấm **Export CSV** để có `labels-<tên>.csv`.
4. Khi đủ ba file, chạy:

   ```powershell
   python eval/agreement.py labels-hai-chau.csv labels-yen.csv labels-huyen.csv --output deliverables/evidence/human-agreement-v1.txt
   ```

5. Thảo luận từng case bất đồng, chốt nhãn vàng vào một file 30 rows mới rồi lưu
   thành `deliverables/evidence/labels-gold-v1.csv`. Giữ nguyên `human-agreement-v1.txt` vì con số cần đo
   trước khi đồng thuận.

## GATE 2

**Chưa đạt cho tới khi có ba file nhãn độc lập, con số human–human agreement và danh
sách disagreement thực.** Không thay các dữ liệu này bằng nhãn do AI tạo.
