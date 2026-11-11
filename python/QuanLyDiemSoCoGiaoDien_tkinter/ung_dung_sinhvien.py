import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import csdl_sinhvien as db

class UngDungSinhVien(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản lý sinh viên")
        self.geometry("650x550")
        self.resizable(False, False)

        db.tao_bang_neu_chua_co()

        self.khoi_tao_giao_dien()
        self.tai_lai_danh_sach_sinh_vien()

    def khoi_tao_giao_dien(self):
        khung_nhap = tk.Frame(self)
        khung_nhap.pack(pady=10, padx=10, fill="x")

        tk.Label(khung_nhap, text="Mã sinh viên:").grid(
            row=0, column=0, sticky="w", pady=5
        )
        self.o_nhap_ma_sv = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ma_sv.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Họ tên:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.o_nhap_ho_ten = tk.Entry(khung_nhap, width=30)
        self.o_nhap_ho_ten.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Lớp:").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.o_nhap_lop = tk.Entry(khung_nhap, width=30)
        self.o_nhap_lop.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(khung_nhap, text="Điểm:").grid(
            row=3, column=0, sticky="w", pady=5
        )
        self.o_nhap_diem = tk.Entry(khung_nhap, width=30)
        self.o_nhap_diem.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(
            khung_nhap,
            text="Thêm sinh viên",
            command=self.xu_ly_them_sinh_vien
        ).grid(row=4, column=0, columnspan=2, pady=10)

        khung_danh_sach = tk.Frame(self)
        khung_danh_sach.pack(pady=5, padx=10, fill="both", expand=True)

        self.listbox_sinh_vien = tk.Listbox(
            khung_danh_sach, width=85, height=15
        )
        self.listbox_sinh_vien.pack(
            side="left", fill="both", expand=True
        )

        thanh_cuon = tk.Scrollbar(
            khung_danh_sach,
            orient="vertical",
            command=self.listbox_sinh_vien.yview
        )
        thanh_cuon.pack(side="right", fill="y")
        self.listbox_sinh_vien.config(
            yscrollcommand=thanh_cuon.set
        )

        khung_nut_thao_tac = tk.Frame(self)
        khung_nut_thao_tac.pack(pady=10)

        tk.Button(
            khung_nut_thao_tac,
            text="Xoá sinh viên",
            command=self.xu_ly_xoa_sinh_vien
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            khung_nut_thao_tac,
            text="Thống kê theo lớp",
            command=self.xu_ly_thong_ke
        ).grid(row=0, column=1, padx=5)

    def tai_lai_danh_sach_sinh_vien(self):
        self.listbox_sinh_vien.delete(0, tk.END)
        self.danh_sach_hien_tai = db.lay_toan_bo_sinh_vien()

        for sinh_vien in self.danh_sach_hien_tai:
            id_sv, ma_sv, ho_ten, lop, diem = sinh_vien

            self.listbox_sinh_vien.insert(
                tk.END,
                f"{ma_sv} - {ho_ten} - {lop} - Điểm: {diem}"
            )

    def xu_ly_them_sinh_vien(self):
        ma_sv = self.o_nhap_ma_sv.get().strip()
        ho_ten = self.o_nhap_ho_ten.get().strip()
        lop = self.o_nhap_lop.get().strip()
        diem = self.o_nhap_diem.get().strip()

        if ma_sv == "" or ho_ten == "" or lop == "" or diem == "":
            messagebox.showerror(
                "Lỗi",
                "Vui lòng nhập đầy đủ thông tin sinh viên."
            )
            return

        try:
            diem = float(diem)

            if diem < 0 or diem > 10:
                messagebox.showerror(
                    "Lỗi",
                    "Điểm phải nằm trong khoảng từ 0 đến 10."
                )
                return

            db.them_sinh_vien(ma_sv, ho_ten, lop, diem)

            self.o_nhap_ma_sv.delete(0, tk.END)
            self.o_nhap_ho_ten.delete(0, tk.END)
            self.o_nhap_lop.delete(0, tk.END)
            self.o_nhap_diem.delete(0, tk.END)

            self.tai_lai_danh_sach_sinh_vien()

            messagebox.showinfo(
                "Thành công",
                f"Đã thêm sinh viên: {ho_ten}"
            )

        except ValueError:
            messagebox.showerror(
                "Lỗi",
                "Điểm phải là 1 số."
            )

        except db.sqlite3.IntegrityError:
            messagebox.showerror(
                "Lỗi",
                "Mã sinh viên đã tồn tại."
            )

    def xu_ly_xoa_sinh_vien(self):
        lua_chon = self.listbox_sinh_vien.curselection()

        if not lua_chon:
            messagebox.showerror(
                "Lỗi",
                "Vui lòng chọn 1 sinh viên trong danh sách để xoá."
            )
            return

        id_sinh_vien = self.danh_sach_hien_tai[lua_chon[0]][0]

        db.xoa_sinh_vien(id_sinh_vien)
        self.tai_lai_danh_sach_sinh_vien()

        messagebox.showinfo(
            "Thành công",
            "Đã xoá sinh viên."
        )

    def xu_ly_thong_ke(self):
        du_lieu_thong_ke = db.thong_ke_theo_lop()

        if not du_lieu_thong_ke:
            messagebox.showinfo(
                "Thông báo",
                "Chưa có dữ liệu sinh viên để thống kê."
            )
            return

        cac_lop = [dong[0] for dong in du_lieu_thong_ke]
        diem_trung_binh = [dong[1] for dong in du_lieu_thong_ke]

        plt.figure(figsize=(6, 4))
        plt.bar(cac_lop, diem_trung_binh, color="cornflowerblue")
        plt.title("Điểm trung bình theo lớp")
        plt.xlabel("Lớp")
        plt.ylabel("Điểm trung bình")
        plt.ylim(0, 10)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    ung_dung = UngDungSinhVien()
    ung_dung.mainloop()
