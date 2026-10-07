# ==========================================
# QUAN LY SINH VIEN
# ==========================================

danh_sach_sv = [
    {
        "ma_sv": "SV001",
        "ho_ten": "Nguyen Van An",
        "nam_sinh": 2005,
        "diem_tb": 8.5
    },
    {
        "ma_sv": "SV002",
        "ho_ten": "Tran Thi Binh",
        "nam_sinh": 2005,
        "diem_tb": 7.8
    },
    {
        "ma_sv": "SV003",
        "ho_ten": "Le Van Cuong",
        "nam_sinh": 2004,
        "diem_tb": 9.0
    }
]


# ==========================================
# HAM TIM SINH VIEN THEO MA
# ==========================================

def tim_sinh_vien(ma_sv):
    for sv in danh_sach_sv:
        if sv["ma_sv"] == ma_sv:
            return sv
    return None


# ==========================================
# HAM HIEN THI DANH SACH
# ==========================================

def hien_thi_danh_sach():
    if len(danh_sach_sv) == 0:
        print("\n-> Danh sach sinh vien dang rong.")
        return

    print("\n" + "=" * 75)
    print(f"{'Ma SV':<10}{'Ho ten':<25}{'Nam sinh':<12}{'Diem TB':<10}")
    print("-" * 75)

    for sv in danh_sach_sv:
        print(
            f"{sv['ma_sv']:<10}"
            f"{sv['ho_ten']:<25}"
            f"{sv['nam_sinh']:<12}"
            f"{sv['diem_tb']:<10.2f}"
        )

    print("=" * 75)


# ==========================================
# HAM NHAP SO NGUYEN AN TOAN
# ==========================================

def nhap_so_nguyen(loi_nhac):
    while True:
        try:
            return int(input(loi_nhac))
        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap mot so nguyen.")


# ==========================================
# HAM NHAP DIEM AN TOAN
# ==========================================

def nhap_diem():
    while True:
        try:
            diem = float(input("Nhap diem trung binh: "))

            if 0 <= diem <= 10:
                return diem

            print("-> Diem phai nam trong khoang tu 0 den 10.")

        except ValueError:
            print("-> Du lieu khong hop le, vui long nhap mot so.")


# ==========================================
# HAM THEM SINH VIEN
# ==========================================

def them_sinh_vien():
    print("\n--- THEM SINH VIEN ---")

    ma_sv = input("Nhap ma sinh vien: ").strip().upper()

    if tim_sinh_vien(ma_sv) is not None:
        print(f"-> Ma sinh vien {ma_sv} da ton tai.")
        return

    ho_ten = input("Nhap ho ten: ").strip().title()

    nam_sinh = nhap_so_nguyen("Nhap nam sinh: ")

    diem_tb = nhap_diem()

    sinh_vien = {
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "nam_sinh": nam_sinh,
        "diem_tb": diem_tb
    }

    danh_sach_sv.append(sinh_vien)

    print(f"-> Da them sinh vien {ma_sv} thanh cong.")


# ==========================================
# HAM TIM KIEM SINH VIEN
# ==========================================

def tim_kiem_sinh_vien():
    print("\n--- TIM KIEM SINH VIEN ---")

    ma_sv = input("Nhap ma sinh vien can tim: ").strip().upper()

    sv = tim_sinh_vien(ma_sv)

    if sv is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    print("\nThong tin sinh vien:")
    print(f"Ma SV    : {sv['ma_sv']}")
    print(f"Ho ten   : {sv['ho_ten']}")
    print(f"Nam sinh : {sv['nam_sinh']}")
    print(f"Diem TB  : {sv['diem_tb']:.2f}")


# ==========================================
# HAM SUA SINH VIEN
# ==========================================

def sua_sinh_vien():
    print("\n--- SUA THONG TIN SINH VIEN ---")

    ma_sv = input("Nhap ma sinh vien can sua: ").strip().upper()

    sv = tim_sinh_vien(ma_sv)

    if sv is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    print("Nhap thong tin moi:")

    ho_ten = input("Nhap ho ten moi: ").strip().title()
    nam_sinh = nhap_so_nguyen("Nhap nam sinh moi: ")
    diem_tb = nhap_diem()

    sv["ho_ten"] = ho_ten
    sv["nam_sinh"] = nam_sinh
    sv["diem_tb"] = diem_tb

    print(f"-> Da cap nhat sinh vien {ma_sv} thanh cong.")


# ==========================================
# HAM XOA SINH VIEN
# ==========================================

def xoa_sinh_vien():
    print("\n--- XOA SINH VIEN ---")

    ma_sv = input("Nhap ma sinh vien can xoa: ").strip().upper()

    sv = tim_sinh_vien(ma_sv)

    if sv is None:
        print(f"-> Khong tim thay sinh vien {ma_sv}.")
        return

    danh_sach_sv.remove(sv)

    print(f"-> Da xoa sinh vien {ma_sv} thanh cong.")


# ==========================================
# HAM THONG KE
# ==========================================

def thong_ke():
    if len(danh_sach_sv) == 0:
        print("\n-> Chua co sinh vien nao.")
        return

    tong_diem = 0

    for sv in danh_sach_sv:
        tong_diem += sv["diem_tb"]

    diem_trung_binh = tong_diem / len(danh_sach_sv)

    so_sinh_vien_gioi = 0

    for sv in danh_sach_sv:
        if sv["diem_tb"] >= 8:
            so_sinh_vien_gioi += 1

    print("\n--- THONG KE ---")
    print(f"Tong so sinh vien : {len(danh_sach_sv)}")
    print(f"Diem TB chung     : {diem_trung_binh:.2f}")
    print(f"Sinh vien dat >= 8: {so_sinh_vien_gioi}")


# ==========================================
# HAM HIEN THI MENU
# ==========================================

def hien_thi_menu():
    print("\n")
    print("=" * 45)
    print("       QUAN LY SINH VIEN")
    print("=" * 45)
    print("1. Hien thi danh sach sinh vien")
    print("2. Tim kiem sinh vien")
    print("3. Them sinh vien")
    print("4. Sua thong tin sinh vien")
    print("5. Xoa sinh vien")
    print("6. Thong ke")
    print("0. Thoat")
    print("=" * 45)


# ==========================================
# HAM CHAY CHUONG TRINH
# ==========================================

def chay_chuong_trinh():
    while True:
        hien_thi_menu()

        lua_chon = input("Nhap lua chon cua ban: ").strip()

        if lua_chon == "1":
            hien_thi_danh_sach()

        elif lua_chon == "2":
            tim_kiem_sinh_vien()

        elif lua_chon == "3":
            them_sinh_vien()

        elif lua_chon == "4":
            sua_sinh_vien()

        elif lua_chon == "5":
            xoa_sinh_vien()

        elif lua_chon == "6":
            thong_ke()

        elif lua_chon == "0":
            print("Cam on da su dung chuong trinh. Tam biet!")
            break

        else:
            print("-> Lua chon khong hop le, vui long chon lai.")


# ==========================================
# CHAY CHUONG TRINH
# ==========================================

if __name__ == "__main__":
    chay_chuong_trinh()