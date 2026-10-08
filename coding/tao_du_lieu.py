"""Sinh bộ dữ liệu mô phỏng: khảo sát sinh viên (dataset/sinh_vien.csv).

Dữ liệu là dữ liệu TỰ TẠO (mô phỏng), không phải số liệu khảo sát thật.
Cố định seed để chạy lại luôn ra đúng một file.
"""

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 3031
N = 200
OUT = Path(__file__).resolve().parents[1] / "dataset" / "sinh_vien.csv"

rng = np.random.default_rng(SEED)

# --- Biến định tính ---
gioi_tinh = rng.choice(["Nam", "Nữ"], size=N, p=[0.6, 0.4])
nganh = rng.choice(
    ["Toán tin", "CNTT", "Kinh tế", "Cơ khí"], size=N, p=[0.25, 0.35, 0.2, 0.2]
)
lam_them = rng.choice(["Có", "Không"], size=N, p=[0.4, 0.6])

la_nam = gioi_tinh == "Nam"
co_lam_them = lam_them == "Có"

# --- Biến định lượng ---
# Chiều cao (cm): chuẩn theo từng giới
chieu_cao = np.where(la_nam, rng.normal(169, 6, N), rng.normal(157, 5.5, N))

# Cân nặng (kg): phụ thuộc tuyến tính vào chiều cao + nhiễu
can_nang = 0.75 * (chieu_cao - 100) + np.where(la_nam, 8, 2) + rng.normal(0, 6, N)

# Số giờ tự học mỗi tuần: sinh viên đi làm thêm học ít hơn một chút
gio_tu_hoc = rng.normal(16, 5, N) - np.where(co_lam_them, 3, 0)
gio_tu_hoc = np.clip(gio_tu_hoc, 1, None)

# GPA (thang 4): tăng theo giờ tự học + nhiễu
gpa = 2.0 + 0.06 * gio_tu_hoc + rng.normal(0, 0.4, N)
gpa = np.clip(gpa, 1.0, 4.0)

df = pd.DataFrame(
    {
        "ma_sv": [f"SV{i:03d}" for i in range(1, N + 1)],
        "gioi_tinh": gioi_tinh,
        "nganh": nganh,
        "lam_them": lam_them,
        "chieu_cao_cm": chieu_cao.round(1),
        "can_nang_kg": can_nang.round(1),
        "gio_tu_hoc_tuan": gio_tu_hoc.round(1),
        "gpa": gpa.round(2),
    }
)

OUT.parent.mkdir(exist_ok=True)
# utf-8-sig để Excel mở không lỗi dấu tiếng Việt
df.to_csv(OUT, index=False, encoding="utf-8-sig")

print(f"Đã ghi {len(df)} dòng -> {OUT}")
