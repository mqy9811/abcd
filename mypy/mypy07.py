# coding=utf-8
"""
    计算机
"""
from tkinter import *
from tkinter import messagebox

class Calculator(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.calculator_widget()

    def calculator_widget(self):
        """计算器布局"""
        btn_text = (("MC", "M+", "M-", "MR"),
                    ("C", "±", "/", "*"),
                    (7, 8, 9, "-"),
                    (4, 5, 6, "+"),
                    (1, 2, 3, "="),
                    (0, "."))
        Entry(self).grid(row=0, column=0, columnspan=4)
        for row_num, n in enumerate(btn_text):
            for column_num, m in enumerate(btn_text[row_num]):
                if m == 0:
                    Button(self, text=m, width=2).grid(row=row_num + 1, column=column_num, columnspan=2, sticky=NSEW)
                elif m == "=":
                    Button(self, text=m, width=2).grid(row=row_num + 1, rowspan=2, column=column_num, sticky=NSEW)
                elif m == ".":
                    Button(self, text=m, width=2).grid(row=row_num + 1, column=column_num+1, sticky=NSEW)
                else:
                    Button(self, text=m, width=2).grid(row=row_num+1, column=column_num, sticky=NSEW)


if __name__ == "__main__":
    root = Tk()
    root.title("计算器")
    root.geometry("170x220+200+100")
    app = Calculator(master=root)
    root.mainloop()
