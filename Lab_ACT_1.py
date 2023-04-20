from tkinter import*

class MyWindow:
    def __init__(self,win):
        self.title1 = Label(win, text="Laboratory Activity 5", font="Verdana")
        self.title1.place(x=150, y=25)
        self.title2 = Label(win, text="Submitted to: Mam Sayo", font="Verdana")
        self.title2.place(x=150, y=50)

window = Tk()
mywin = MyWindow(window)
window.geometry("500x100+10+10")
window.title("Label")
window.mainloop()