import tkinter as tk
from tkinter import messagebox
import subprocess

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 18), bd=10, insertwidth=4, width=15, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        for (text, row, column) in buttons:
            tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda t=text: self.on_button_click(t)).grid(row=row, column=column)

        self.root.bind("<Alt-F7>", self.show_menu)

    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
                self.result_var.set("")
        else:
            self.result_var.set(self.result_var.get() + str(char))

    def show_menu(self, event):
        subprocess.Popen(["python", "calcecxt2.py"])

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
