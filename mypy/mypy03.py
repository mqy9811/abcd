# coding=utf-8
"""
    label的功能测试
"""
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """主程序界面"""

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.app_widget()
        self.pack()

    def app_widget(self):
        label01 = Label(self, text="努力奋斗，拼搏向上！", bg="orange", fg="red")
        label01.pack()

        # 图片（tkinter只允许有.jpg的图片插入）
        global picture01
        picture01 = PhotoImage(file="../GIF/ball.png")
        label02 = Label(self, image=picture01)
        label02.pack()


if __name__ == "__main__":
    root = Tk()
    root.title("label的测试")
    root.geometry("300x200+200+100")
    app = Application(master=root)
    root.mainloop()
