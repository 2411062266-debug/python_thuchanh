
import tkinter as tk
from tkinter import messagebox
import ast
import operator

CAC_PHEP_TOAN = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos
}

def tinh_bieu_thuc(node):
    if isinstance(node, ast.Expression):
        return tinh_bieu_thuc(node.body)

    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in CAC_PHEP_TOAN:
        phep_toan = CAC_PHEP_TOAN[type(node.op)]
        trai = tinh_bieu_thuc(node.left)
        phai = tinh_bieu_thuc(node.right)
        return phep_toan(trai, phai)

    if isinstance(node, ast.UnaryOp) and type(node.op) in CAC_PHEP_TOAN:
        return CAC_PHEP_TOAN[type(node.op)](
            tinh_bieu_thuc(node.operand)
        )

    raise ValueError("Bieu thuc khong hop le")

def bam_nut(ky_tu):
    if ky_tu == "=":
        try:
            bieu_thuc = o_hien_thi.get()
            cay = ast.parse(bieu_thuc, mode="eval")
            ket_qua = tinh_bieu_thuc(cay)
            o_hien_thi.set(str(ket_qua))

        except ZeroDivisionError:
            messagebox.showerror("Loi", "Khong the chia cho 0.")

        except (SyntaxError, ValueError, TypeError):
            messagebox.showerror("Loi", "Bieu thuc khong hop le.")

    elif ky_tu == "C":
        o_hien_thi.set("")

    else:
        o_hien_thi.set(o_hien_thi.get() + ky_tu)

cua_so = tk.Tk()
cua_so.title("May tinh bo tui")
cua_so.geometry("320x390")
cua_so.resizable(False, False)

o_hien_thi = tk.StringVar()

tk.Entry(
    cua_so,
    textvariable=o_hien_thi,
    font=("Arial", 18),
    justify="right",
    state="readonly"
).grid(
    row=0, column=0, columnspan=4,
    padx=10, pady=15, ipady=8, sticky="nsew"
)

cac_nut = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("C", "0", "=", "+")
]

for r, hang in enumerate(cac_nut, start=1):
    for c, ky_tu in enumerate(hang):
        tk.Button(
            cua_so,
            text=ky_tu,
            font=("Arial", 14),
            width=5,
            height=2,
            command=lambda k=ky_tu: bam_nut(k)
        ).grid(
            row=r, column=c, padx=4, pady=4, sticky="nsew"
        )

cua_so.mainloop()
