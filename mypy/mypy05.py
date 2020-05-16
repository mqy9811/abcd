# coding=utf-8

"""文本输入测试、单复选框测试"""

from tkinter import *
from tkinter import messagebox
import webbrowser


class TextChoice(Frame):
    """文本"""
    def __init__(self, master=None):
        super().__init__(master)
        self.w1 = Text(self, width=45, height=26, bg="white")
        self.master = master
        self.setwigetview()
        self.pack()

    def setwigetview(self):
        """在self中布局组件"""
        self.w1.pack()
        Button(self, command=self.inserttxt, text="插入文本").pack(side="left")
        Button(self, command=self.returntxt, text="返回文本").pack(side="left")
        Button(self, command=self.addwidget, text="添加组件").pack(side="left")
        Button(self, command=self.tag, text="精确文本编辑").pack(side="left")
        Button(self, command=self.insertimage, text="插入图片").pack(side="left")

    def text_widget(self):
        """MAIN TEXT"""
        pass

    def inserttxt(self):
        """重复插入文本插入"""
        self.w1.insert(INSERT, "学习Python，使我开心\n")  # 光标处插入
        self.w1.insert(END, "\n当我学习结束了，我希望找到一份好个工作！=.= !")

    def returntxt(self):
        """返回所有文本"""
        print("返回所有文本：\n"+self.w1.get(1.0, END))

    def insertimage(self):
        """插入图片"""
        self.photo = PhotoImage(file="../GIF/smile.gif")
        self.w1.image_create(END, image=self.photo)

    def addwidget(self):
        """插入组件"""
        b1 = Button(self, text="认真学习", bg="red").pack(side="right")
        self.w1.window_create(INSERT, window=b1)

    def tag(self):
        """tag精确控制文本"""
        self.w1.delete(1.0, END)
        self.w1.insert(INSERT, "岁月静好，只是催人老！\n明月高悬，只能寄相思！\n形单影只，又有何人知！\n百度一下")
        self.w1.tag_add("诗句", 1.0, 1.11)
        self.w1.tag_config("诗句", background="gray")
        self.w1.tag_add("bai_du", 4.0, END)
        self.w1.tag_bind("bai_du", "<Button-1>", self.webshow)

    def webshow(self, event):
        """打开浏览器"""
        webbrowser.open("http://www.baidu.com")


class Choice(Frame):
    """选择框"""
    def __init__(self, master=None):
        super().__init__(master)
        self.playgame = IntVar()
        self.hardwork = IntVar()
        self.value = StringVar()
        self.master = master
        self.choice_widget()
        self.pack()

    def choice_widget(self):
        """选择框"""
        self.checkbox()
        self.radiobox()

    def radiobox(self):
        """单选"""
        self.value.set("F")

        Radiobutton(self, text="男性", value="M", variable=self.value).grid(row=0, column=0, sticky=W)
        Radiobutton(self, text="女性", value="F", variable=self.value).grid(row=0, column=1, sticky=W)
        Button(self, text="确认", command=self.confirm).grid(row=1, column=3, sticky=E)

    def checkbox(self):
        """多选"""

        Checkbutton(self, text="努力学习，多敲代码", variable=self.hardwork, onvalue=1, offvalue=0).grid(row=1, column=0)
        Checkbutton(self, text="游戏中放松身心，为了更好的工作！", variable=self.playgame, onvalue=1, offvalue=0).grid(row=1, column=1)

    def confirm(self):
        if self.value.get() == "F":
            messagebox.showinfo("message", "你是女性，未来多种多样，尽情绽放自己的美好吧！")
        elif self.value.get() == "M":
            messagebox.showinfo("message", "你是个男生，追求美好生活要好好奋斗！")

        if self.playgame.get() == 1:
            messagebox.showinfo("message", "玩游戏真开心，我要更加认真地敲代码！")

        if self.hardwork.get() == 1:
            messagebox.showinfo("message", "努力工作真辛苦，但是为了未来，值了！")

        if self.hardwork.get() == self.playgame.get() == 0:
            messagebox.showinfo("message", "啥也没干，不是宅男，就是腐女")


if __name__ == "__main__":
    root = Tk()
    root.title("文本及选择")
    root.geometry("500x400+200+100")
    app = Choice(master=root)
    root.mainloop()
