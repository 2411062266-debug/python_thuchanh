so_luot_truy_cap = 0


def tang_luot_truy_cap():
    global so_luot_truy_cap
    so_luot_truy_cap += 1


def vi_du_bien_local():
    so_luot_truy_cap = 100
    print(f"Ben trong ham, bien local = {so_luot_truy_cap}")


tang_luot_truy_cap()
tang_luot_truy_cap()

print(f"So luot truy cap (global): {so_luot_truy_cap}")

vi_du_bien_local()

print(f" Sau khi goi ham, bien global van la: {so_luot_truy_cap}")
# HĐ5.1 - map + lambda

ds = [1, 2, 3, 4, 5]

binh_phuong = list(map(lambda x: x ** 2, ds))

print(binh_phuong)


# HĐ5.2 - filter + lambda

so_chan = list(filter(lambda x: x % 2 == 0, ds))

print(so_chan)


# HĐ5.3 - sorted + lambda

sinh_vien = [
    {"ten": "An", "diem": 8.5},
    {"ten": "Binh", "diem": 7.0},
    {"ten": "Chi", "diem": 9.2}
]


sap_xep_tang = sorted(
    sinh_vien,
    key=lambda sv: sv["diem"]
)

for sv in sap_xep_tang:
    print(f"{sv['ten']} - {sv['diem']}")


print("--- Giam dan ---")


sap_xep_giam = sorted(
    sinh_vien,
    key=lambda sv: sv["diem"],
    reverse=True
)

for sv in sap_xep_giam:
    print(f"{sv['ten']} - {sv['diem']}")