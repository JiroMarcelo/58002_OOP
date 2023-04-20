from tkinter import *

class MyWindow:
    def __init__(self, win):
        self.win = win
        self.cb = Label(win, text="Color", font="Vendara", bg="yellow", fg="red", relief="raised", borderwidth=2, width=5)
        self.cb.bind("<Button>", self.change_color)
        self.cb.place(x=50, y=150)
        self.color_text = Label(win, text="<--- Click to change the color of the button", font="Vendara", bg="white", fg="black", relief="raised", borderwidth=1, width=40)
        self.color_text.place(x=110, y=150)

    def change_color(self, event):
        self.cb.config(bg='blue')

window = Tk()
mywin = MyWindow(window)
window.geometry("500x200+10+10")
window.title("Button")
window.mainloop()