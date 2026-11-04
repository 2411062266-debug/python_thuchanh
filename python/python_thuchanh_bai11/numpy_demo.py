
import numpy as np

diem_list = [2.3, 9.0, 8.2, 10.0, 4.3]
diem_array = np.array(diem_list)

print(type(diem_list), type(diem_array))

diem_cong_them = diem_array + 0.5
print(diem_cong_them)

diem_cong_them_list = [diem + 0.5 for diem in diem_list]
print(diem_cong_them_list)

print("Trung binh:", np.mean(diem_array))
print("Lon nhat:", np.max(diem_array))
print("Nho nhat:", np.min(diem_array))
print("Do lech chuan:", round(np.std(diem_array), 2))

ma_tran = np.array([[5, 6, 7], [2, 5, 7]])
print("Ma tran:\n", ma_tran)
print("Kich thuoc (shape):", ma_tran.shape)
print("Ma tran nhan 2:\n", ma_tran * 2)