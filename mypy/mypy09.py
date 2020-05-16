#coding=utf-8
"""
    钢琴
"""
from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.choice()
        self.key()

    def choice(self):
        btn_txt = ["中国风", "日语歌", "私人电台", "古典歌曲"]
        for t in btn_txt:
            Button(self, text=t).pack(side="left", padx=30, ipady=20)

    def key(self):
        pass


if __name__ == "__main__":
    root = Tk()
    root.title("钢琴")
    root.geometry("500x300+200+100")
    app = Application(root)

    root.mainloop()
