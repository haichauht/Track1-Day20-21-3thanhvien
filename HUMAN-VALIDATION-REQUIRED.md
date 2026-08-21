# Human validation required before submission

Bài lab cấm AI tự thay con người ở Phase 2 và verdict/reflection. AI đã hoàn thiện
pipeline và tạo provisional review để tiết kiệm thời gian, nhưng người nộp cần:

1. Mở `deliverables/evidence/report-phase2-hai-chau.html`, chấm độc lập 30 rows và Export CSV. Report này
   đã ẩn judge và nhãn AI để tránh bias. CSV Hải Châu cũ chỉ có 24/30 rows; cần chấm
   thêm sc-25 đến sc-30 trong report mới trước khi dùng để đo agreement. Bản 24 nhãn
   cũ được giữ tại `deliverables/evidence/labels-hai-chau-legacy24.csv`.
2. Đặc biệt đọc sc-02, sc-03, sc-05, sc-07, sc-08, sc-11, sc-12, sc-13, sc-15,
   sc-18, sc-24, đồng thời kiểm kỹ sáu trap sc-25–sc-30.
3. Ba người mở report mang tên mình trong `deliverables/evidence/`, export file riêng
   rồi chạy `python eval/agreement.py ...`; thay N/A trong mục 5/7 của REPORT bằng agreement thật và ghi
   disagreement cases.
4. Đọc mục 7 trong `deliverables/REPORT.md`, tự xác nhận HOLD và reflection.
5. ~~Thay LangSmith key, xác thực lại và chạy batch để lấy permalink.~~ Hoàn tất ngày
   2026-08-21: 54 trace đã ghi nhận (30 tutor + 24 judge), 0 trace lỗi.

Tracing evidence đã hoàn tất. Người nộp vẫn phải thực hiện bốn bước human validation
ở trên để đáp ứng phần bài không được phép giao cho AI.
