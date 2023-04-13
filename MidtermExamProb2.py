from tkinter import *

class Name:

    def __init__(self, win):
        self.title = Label(win, text="My Full name", font="Verdana", foreground="red")
        self.title.place(x=250, y=20)
        self.l1 = Label(win, text="Enter given name", font="Verdana", foreground="red")
        self.l1.place(x=100, y=100)
        self.in1 = Entry(win, borderwidth=1, width=30)
        self.in1.place(x=350, y=100)
        self.l2 = Label(win, text="Enter Middle name", font="Verdana", foreground="red")
        self.l2.place(x=100, y=150)
        self.in2 = Entry(win, borderwidth=1, width=30)
        self.in2.place(x=350, y=150)
        self.l3 = Label(win, text="Enter Last name", font="Verdana", foreground="red")
        self.l3.place(x=100, y=200)
        self.in3 = Entry(win, borderwidth=1, width=30)
        self.in3.place(x=350, y=200)
        self.btn = Button(win, text=" Show Full name ", command=self.fullname)
        self.btn.place(x=300, y=300)
        self.clear_btn = Button(win, text="      Clear All        ", command=self.clear_entries)
        self.clear_btn.place(x=300, y=350)
        self.fl1 = Label(win, text="Enter My Full Name is:", font="Verdana", foreground="red")
        self.fl1.place(x=100, y=250)
        self.fl2 = Entry(win, bd=3, width=50, foreground="red")
        self.fl2.place(x=350, y=250)

    def fullname(self):
        self.fl2.delete(0, 'end')
        self.first = str(self.in1.get())
        self.middle = str(self.in2.get())
        self.last = str(self.in3.get())
        full = f"{self.last}, {self.first} {self.middle}"
        self.fl2.insert(END, str(full))

    def clear_entries(self):
        self.in1.delete(0, 'end')
        self.in2.delete(0, 'end')
        self.in3.delete(0, 'end')
        self.fl2.delete(0, 'end')


window = Tk()
winn = Name(window)
window.geometry("700x500+20+20")
window.title("My Full Name")
window.mainloop()

