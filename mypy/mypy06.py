# coding=utf-8
"""
    画布测试
"""
from tkinter import *
from tkinter import messagebox
import random

class Canvas01(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.canvas_widget()

    def canvas_widget(self):
        """画布布局"""
        self.canvas = Canvas(self, width=400, height=300, bg="white")
        self.canvas.pack()

        # global photo
        # photo = PhotoImage(file="GIF/smile.gif")
        # self.canvas.create_image(200, 100, image=photo)

        self.canvas.create_line(10,20,130,40,50,10,70,80,190,100)

        Button(self, text="画十个矩形", command=self.draw).pack()

    def draw(self):
        for i in range(0, 10):
            x1 = random.randrange(int(self.canvas["width"])/2)
            y1 = random.randrange(int(self.canvas["height"])/2)

            x2 = random.randrange(int(self.canvas["width"])/2)
            y2 = random.randrange(int(self.canvas["height"])/2)

            self.canvas.create_oval(x1, y1, x2, y2)

if __name__ == "__main__":
    root = Tk()
    root.title("画布测试")
    root.geometry("500x300+200+100")
    app = Canvas01(master=root)
    root.mainloop()
