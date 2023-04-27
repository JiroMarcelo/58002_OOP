import tkinter as tk


class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        self.entry = tk.Entry(self.master, width=30, font=("Vendara", 14), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        for i in range(10):
            if i == 9:
                button = tk.Button(self.master, text=str(0), font=("Vendara", 14),
                                   command=lambda i=i: self.button_click(0))
                button.grid(row=4, column=1, sticky="nsew")
            else:
                button = tk.Button(self.master, text=str(i + 1), font=("Vendara", 14),
                                   command=lambda i=i: self.button_click(i + 1))
                button.grid(row=3 - (i // 3), column=i % 3, sticky="nsew")
            self.master.grid_columnconfigure(i % 3, minsize=75)
            self.master.grid_rowconfigure(3 - (i // 3), minsize=75)

        operators = ["+", "-", "*", "/"]
        for i in range(4):
            button = tk.Button(self.master, text=operators[i], font=("Vendara", 14),
                               command=lambda i=i: self.operator_click(operators[i]))
            button.grid(row=i + 1, column=3, sticky="nsew")
            self.master.grid_columnconfigure(3, minsize=75)
            self.master.grid_rowconfigure(i + 1, minsize=75)

        equal_button = tk.Button(self.master, text="=", font=("Vendara", 14), command=self.equal_click)
        equal_button.grid(row=4, column=2, sticky="nsew")
        self.master.grid_columnconfigure(2, minsize=75)

        clear_button = tk.Button(self.master, text="AC", font=("Vendara", 14), command=self.clear_click)
        clear_button.grid(row=4, column=0, sticky="nsew")
        self.master.grid_columnconfigure(0, minsize=75)

        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

    def button_click(self, number):
        current = self.entry.get()
        new = current + str(number)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, new)

    def operator_click(self, operator):
        current = self.entry.get()
        self.first_num = float(current)
        self.operation = operator
        self.entry.delete(0, tk.END)

    def equal_click(self):
        current = self.entry.get()
        second_num = float(current)
        self.entry.delete(0, tk.END)

        if self.operation == "+":
            result = self.first_num + second_num
        elif self.operation == "-":
            result = self.first_num - second_num
        elif self.operation == "*":
            result = self.first_num * second_num
        elif self.operation == "/":
            result = self.first_num / second_num
        self.entry.insert(0, f"{result}")

    def clear_click(self):
        self.entry.delete(0, tk.END)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()