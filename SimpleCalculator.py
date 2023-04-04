from tkinter import *
class MyWindow:
    def __init__(self,win):

#widgets start from here
        self.lbl1 = Label(win,text="Value 1")     #for label widget
        self.lbl1.place(x=50,y=50)
        self.lbl2 = Label(win, text= "Value 2")
        self.lbl2.place(x=50,y=100)
        self.lbl3 = Label(win, text="Result")
        self.lbl3.place(x=50,y=150)
        label=Label(win,text = "CALCULATOR")
        label.place(x=200,y=10)
        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=120,y=50)
        self.txt2 = Entry(win,bd=1)
        self.txt2.place(x=120,y=100)
        self.txt3 = Entry(win,bd=3)
        self.txt3.place(x=120,y=150)
        self.btnadd = Button(win,text="     Add      ")
        self.btnadd.place(x=300,y=85)
        self.btnadd.bind('<Button-1>',self.add)
        self.btnsub = Button(win,text="  Subtract  ",command = self.sub)
        self.btnsub.place(x=300,y=120)
        self.btnmulti = Button(win,text="  Multiply  ",command = self.multi)
        self.btnmulti.place(x=300,y=155)
        self.btndiv = Button(win,text="    Divide    ",command = self.div)
        self.btndiv.place(x=300,y=190)
        self.btnclr = Button(win, text="    Clear     ", command=self.clr)
        self.btnclr.place(x=300, y=50)


#add event-handling /bind () method

    def add(self,add):
        self.txt3.delete(0,'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 + num2
        self.txt3.insert(END,str(result))

# sub event-handler using command parameter
    def sub(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1-num2
        self.txt3.insert(END, str(result))

    def multi(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 * num2
        self.txt3.insert(END, str(result))

    def div(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        result = num1 / num2
        self.txt3.insert(END, str(result))

    def clr(self):
        self.txt1.delete(0)
        self.txt2.delete(0)
        self.txt3.delete(0, 'end')


window = Tk()
mywin = MyWindow(window)
window.geometry("500x400+10+10")
window.title("Simple Calculator")
window.mainloop()







