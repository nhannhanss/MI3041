# Bộ dữ liệu `sinh_vien.csv`

## 1. Bối cảnh và ý nghĩa

Bộ dữ liệu mô phỏng một cuộc khảo sát 200 sinh viên đại học về thể trạng (chiều cao, cân nặng) và việc học (số giờ tự học mỗi tuần, điểm GPA), kèm thông tin giới tính, ngành học và việc đi làm thêm.

Đây là **dữ liệu tự tạo bằng mô phỏng**, không phải số liệu khảo sát thật. Dữ liệu được sinh bởi script `coding/tao_du_lieu.py` với seed cố định (3031), nên chạy lại script luôn cho ra đúng file này.

Mỗi dòng là một sinh viên. Bộ dữ liệu dùng để thực hành ước lượng khoảng tin cậy cho kỳ vọng, phương sai, tỷ lệ và hiệu hai kỳ vọng.

## 2. Thông tin chung

| Mục | Giá trị |
|---|---|
| Số quan sát | 200 |
| Số biến | 8 (1 định danh, 3 định tính, 4 định lượng) |
| Giá trị thiếu | Không có |
| Định dạng | CSV, mã hóa UTF-8 có BOM, dấu phân cách là dấu phẩy |

## 3. Phân loại các biến

| Biến | Loại | Thang đo | Đơn vị / giá trị | Ý nghĩa |
|---|---|---|---|---|
| `ma_sv` | Định danh | – | SV001–SV200 | Mã sinh viên, không dùng để phân tích |
| `gioi_tinh` | Định tính (nhị phân) | Định danh | Nam, Nữ | Giới tính |
| `nganh` | Định tính | Định danh | CNTT, Toán tin, Cơ khí, Kinh tế | Ngành học |
| `lam_them` | Định tính (nhị phân) | Định danh | Có, Không | Sinh viên có đi làm thêm hay không |
| `chieu_cao_cm` | Định lượng (liên tục) | Tỷ lệ | cm | Chiều cao |
| `can_nang_kg` | Định lượng (liên tục) | Tỷ lệ | kg | Cân nặng |
| `gio_tu_hoc_tuan` | Định lượng (liên tục) | Tỷ lệ | giờ/tuần | Số giờ tự học trung bình mỗi tuần |
| `gpa` | Định lượng (liên tục) | Khoảng | thang 4 | Điểm trung bình tích lũy |

## 4. Thống kê mô tả

### Biến định lượng

| Biến | Trung bình | Độ lệch chuẩn | Nhỏ nhất | Trung vị | Lớn nhất |
|---|---|---|---|---|---|
| `chieu_cao_cm` | 164,69 | 7,92 | 144,6 | 165,2 | 183,6 |
| `can_nang_kg` | 54,06 | 9,93 | 31,7 | 53,8 | 77,8 |
| `gio_tu_hoc_tuan` | 15,11 | 5,37 | 1,0 | 15,15 | 31,7 |
| `gpa` | 2,93 | 0,51 | 1,64 | 2,91 | 4,00 |

### Biến định tính

| Biến | Tần số |
|---|---|
| `gioi_tinh` | Nam: 132 (66,0%), Nữ: 68 (34,0%) |
| `nganh` | CNTT: 80, Toán tin: 48, Cơ khí: 38, Kinh tế: 34 |
| `lam_them` | Có: 79 (39,5%), Không: 121 (60,5%) |

## 5. Cách dữ liệu được sinh ra

Ba biến định tính được chọn ngẫu nhiên, độc lập với nhau:

- `gioi_tinh`: Nam với xác suất 0,6; Nữ 0,4.
- `nganh`: Toán tin 0,25; CNTT 0,35; Kinh tế 0,2; Cơ khí 0,2.
- `lam_them`: Có với xác suất 0,4; Không 0,6.

Bốn biến định lượng được sinh từ phân phối chuẩn:

- `chieu_cao_cm`: Nam theo N(169; 6²), Nữ theo N(157; 5,5²).
- `can_nang_kg` = 0,75 × (chiều cao − 100) + 8 (Nam) hoặc + 2 (Nữ) + nhiễu N(0; 6²).
- `gio_tu_hoc_tuan`: N(16; 5²), sinh viên có làm thêm bị trừ 3 giờ; giá trị nhỏ hơn 1 được đặt bằng 1.
- `gpa` = 2,0 + 0,06 × giờ tự học + nhiễu N(0; 0,4²); giá trị được chặn trong đoạn [1; 4].

Chiều cao và cân nặng làm tròn 1 chữ số thập phân, GPA làm tròn 2 chữ số.

## 6. Lưu ý khi phân tích

- Chiều cao trong **từng giới** có phân phối chuẩn, nhưng gộp cả hai giới là hỗn hợp hai phân phối chuẩn. Khoảng tin cậy cho phương sai (dùng phân phối khi bình phương) cần giả thiết chuẩn, nên chỉ nên tính trong một giới.
- `gio_tu_hoc_tuan` và `gpa` bị chặn biên nên không chuẩn tuyệt đối; với n = 200, khoảng tin cậy cho kỳ vọng vẫn áp dụng được nhờ định lý giới hạn trung tâm.
- Vì là dữ liệu mô phỏng, các kết luận chỉ có ý nghĩa minh họa phương pháp, không phản ánh sinh viên thực tế.
