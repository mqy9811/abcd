# coding=utf-8

from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("我的第一个GUI程序")
root.geometry("500x300+300+200")

btn01 = Button(root)
btn01["text"] = "送你一束花！"
btn01.pack()


def gift(e):
    """
    btn01的提示按钮反馈
    """
    messagebox.showinfo("Message", "请你嫁给我！")
    print("hahaha")


btn01.bind("<Button-1>", gift)

root.mainloop()          # 进入组件方法mainloop进行事件循环

print(gift.__doc__)
