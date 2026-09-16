sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

print(sinh_vien["ho_ten"])
print(sinh_vien.get("diem_tb"))
print(sinh_vien.get("lop", "Chua co"))
sinh_vien = {
    "ho_ten": "Nguyen Van A",
    "nam_sinh": 2004,
    "diem_tb": 8.5
}

# Thêm khóa mới
sinh_vien["lop"] = "CNTT01"

# Sửa giá trị
sinh_vien["diem_tb"] = 9.0

print(sinh_vien)

# Xóa khóa
diem_cu = sinh_vien.pop("diem_tb")

print(sinh_vien, "- diem da xoa:", diem_cu)

# Cập nhật / thêm nhiều khóa
sinh_vien.update({
    "nam_sinh": 2003,
    "email": "a@example.com"
})

print(sinh_vien)
diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}

# Duyệt các khóa
for mon in diem_mon_hoc.keys():
    print(mon)

# Duyệt các giá trị
for diem in diem_mon_hoc.values():
    print(diem)

# Duyệt cả khóa và giá trị
for mon, diem in diem_mon_hoc.items():
    print(f"{mon}: {diem}")

# Tính điểm trung bình
tong_diem = 0

for diem in diem_mon_hoc.values():
    tong_diem = tong_diem + diem

print("Diem trung binh:", round(tong_diem / len(diem_mon_hoc), 2))
diem_mon_hoc = {
    "Toan": 8.0,
    "Ly": 7.5,
    "Hoa": 9.0,
    "Van": 6.5
}

diem_cong_diem = {
    mon: round(diem + 0.5, 2)
    for mon, diem in diem_mon_hoc.items()
}

print(diem_cong_diem)

ten_mon_viet_hoa = {
    mon.upper(): diem
    for mon, diem in diem_mon_hoc.items()
}

print(ten_mon_viet_hoa)
mon_hoc_ky1 = {"Toan", "Ly", "Hoa", "Van"}
mon_hoc_ky2 = {"Toan", "Anh", "Tin", "Van"}

print(mon_hoc_ky1 & mon_hoc_ky2)

print(mon_hoc_ky1 | mon_hoc_ky2)

print(mon_hoc_ky1 - mon_hoc_ky2)

