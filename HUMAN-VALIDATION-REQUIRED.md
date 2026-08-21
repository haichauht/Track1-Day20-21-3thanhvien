# Human validation required before submission

Bài lab cấm AI tự thay con người ở Phase 2 và verdict/reflection. AI đã hoàn thiện
pipeline và tạo provisional review để tiết kiệm thời gian, nhưng người nộp cần:

1. `deliverables/evidence/labels-hai-chau.csv` đã đủ 30 rows. Yến và Huyền cần mở
   report blind mang tên mình, chấm đủ 30 rows và Export CSV riêng.
2. Đặc biệt đọc sc-02, sc-03, sc-05, sc-07, sc-08, sc-11, sc-12, sc-13, sc-15,
   sc-18, sc-24, đồng thời kiểm kỹ sáu trap sc-25–sc-30.
3. Ba người mở report mang tên mình trong `deliverables/evidence/`, export file riêng
   rồi chạy `python eval/agreement.py ...`; thay N/A trong mục 5/7 của REPORT bằng agreement thật và ghi
   disagreement cases.
4. Đọc mục 7 trong `deliverables/REPORT.md`, tự xác nhận HOLD và reflection.
5. Tutor canonical đã có đủ 30 trace, 0 lỗi. Judge chỉ chạy lại trên đủ 30 rows sau
   khi có human gold.

Tracing evidence của tutor đã hoàn tất. Người nộp vẫn phải hoàn tất hai file nhãn còn
lại, agreement, human gold và judge calibration 30 rows trước khi nộp.
