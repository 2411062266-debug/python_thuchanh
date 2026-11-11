import sqlite3

TEN_FILE_CSDL = "sinhvien.db"

def ket_noi_csdl():
    return sqlite3.connect(TEN_FILE_CSDL)

def tao_bang_neu_chua_co():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        CREATE TABLE IF NOT EXISTS sinhvien (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ma_sv TEXT NOT NULL UNIQUE,
            ho_ten TEXT NOT NULL,
            lop TEXT NOT NULL,
            diem REAL NOT NULL
        )
    """)
    ket_noi.commit()
    ket_noi.close()

def them_sinh_vien(ma_sv, ho_ten, lop, diem):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "INSERT INTO sinhvien (ma_sv, ho_ten, lop, diem) VALUES (?, ?, ?, ?)",
        (ma_sv, ho_ten, lop, diem)
    )
    ket_noi.commit()
    ket_noi.close()

def lay_toan_bo_sinh_vien():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "SELECT id, ma_sv, ho_ten, lop, diem FROM sinhvien ORDER BY id"
    )
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua

def xoa_sinh_vien(id_sinh_vien):
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute(
        "DELETE FROM sinhvien WHERE id = ?", (id_sinh_vien,)
    )
    ket_noi.commit()
    ket_noi.close()

def thong_ke_theo_lop():
    ket_noi = ket_noi_csdl()
    con_tro = ket_noi.cursor()
    con_tro.execute("""
        SELECT lop, AVG(diem)
        FROM sinhvien
        GROUP BY lop
    """)
    ket_qua = con_tro.fetchall()
    ket_noi.close()
    return ket_qua
