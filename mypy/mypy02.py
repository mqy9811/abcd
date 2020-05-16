# coding=utf-8
"""
    一个典型的GUI的程序
"""
from tkinter import *
from tkinter import messagebox


def present():
    messagebox.showinfo("消息", "送你一个拥抱，未来无限美好")


class Application(Frame):
    """整体实现类"""
    def __init__(self, master=None):
        """初始化"""
        super().__init__(master)
        self.master = master
        self.pack()

        self.create_widget()

    def create_widget(self):
        """建立框架"""
        btn01 = Button(self)     # 欢迎按钮
        btn01["text"] = "点我欢迎你"
        btn01["command"] = present
        btn01.pack()

        btn02 = Button(self, text="退出", command=root.destroy)     #退出按钮
        btn02.pack()


if __name__ == '__main__':
    root = Tk()
    root.title("经典的GUI程序")
    root.geometry("500x300+400+300")
    app = Application(master=root)
    root.mainloop()


