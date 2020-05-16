# coding=utf-8
"""
    扑克牌
"""
from tkinter import *
from tkinter import messagebox

class Puke(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.show_puke()

    def show_puke(self):
        """展示"""
        self.photos = [PhotoImage(file="GIF/puke"+str(i+1)+".gif")for i in range(10)]
        self.labels = [Label(self.master, image=self.photos[i])for i in range(10)]
        for i in range(10):
            self.labels[i].place(x=30*i+10, y=50)
        self.labels[0].bind_class("Label", "<1>", self.action_puke)
    def action_puke(self, event):
        """扑克牌的点击操作"""
        # print(event.widget.winfo_geometry())
        # print(event.widget.winfo_y())
        if event.widget.winfo_y() == 50:
            event.widget.place(y=30)
        else:
            event.widget.place(y=50)


if __name__ == "__main__":
    root = Tk()
    root.title("扑克牌")
    root.geometry("450x300+200+100")
    app = Puke(master=root)
    root.mainloop()
