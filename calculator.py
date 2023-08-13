import tkinter as tk
from tkinter import ttk
from math import *

class Calculator:
    def __init__(self, root):
        self.root = root
        self.expression = ""
        self.display = tk.Entry(root, width=30, font=("Helvetica", 20))
        self.display.grid(row=0, column=0, columnspan=4)

        # Create buttons for the numbers 0-9
        for i in range(10):
            btn = ttk.Button(root, text=str(i), command=lambda x=i: self.add_number(x))
            btn.grid(row=i+1, column=0)

        # Create buttons for the mathematical operations
        btn_add = ttk.Button(root, text="+", command=self.add)
        btn_subtract = ttk.Button(root, text="-", command=self.subtract)
        btn_multiply = ttk.Button(root, text="*", command=self.multiply)
        btn_divide = ttk.Button(root, text="/", command=self.divide)
        btn_clear = ttk.Button(root, text="Clear", command=self.clear)
        btn_equal = ttk.Button(root, text="=", command=self.evaluate)

        btn_add.grid(row=1, column=1)
        btn_subtract.grid(row=1, column=2)
        btn_multiply.grid(row=1, column=3)
        btn_divide.grid(row=2, column=1)
        btn_clear.grid(row=2, column=2)
        btn_equal.grid(row=2, column=3)

    def add_number(self, number):
        self.expression += str(number)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def add(self):
        self.expression += "+"
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def subtract(self):
        self.expression += "-"
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def multiply(self):
        self.expression += "*"
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def divide(self):
        self.expression += "/"
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def power(self):
            self.expression += "^"
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)

    def evaluate(self):
        try:
            result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error: " + str(e))


root = tk.Tk()
root.title("Calculator")
calc = Calculator(root)
root.mainloop()
