# coding=utf-8
"""
    简单登录界面实现
"""
from tkinter import *
from tkinter import messagebox
name = []
pwd = []


class Application(Frame):
    """
    MAIN APP
    """
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.show_widget()
        self.pack()

    def show_widget(self):
        """登录界面"""
        label01 = Label(self, text="用户名")
        label01.pack()

        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()

        label02 = Label(self, text="密码")
        label02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2, show="*")
        self.entry02.pack()

        btn = Button(self, text="登录", command=self.login)
        btn.pack()

    def login(self):
        """登录功能"""
        name.append(self.entry01.get())
        pwd.append(self.entry02.get())

        messagebox.showinfo("登录成功！", "欢迎回来，{0}!".format(name[0]))


if __name__ == "__main__":
    master = Tk()
    master.title("登录测试！")
    master.geometry("500x300+200+100")
    app = Application(master)

    master.mainloop()
    print("用户名：{0}  密码：{1}".format(name, pwd))
