import tkinter as tk
from tkinter import messagebox
import random

class MemoryMatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Match")
        self.cards = ["A", "A", "B", "B", "C", "C", "D", "D", "E", "E", "F", "F"]
        random.shuffle(self.cards)
        self.buttons = []
        self.selected = []
        self.create_buttons()

    def create_buttons(self):
        for i in range(3):
            for j in range(4):
                button = tk.Button(self.root, text=" ", font=("Helvetica", 20), width=3, height=2,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)

    def on_click(self, row, col):
        index = row * 4 + col
        if index not in self.selected:
            self.buttons[index].config(text=self.cards[index])
            self.selected.append(index)
            if len(self.selected) == 2:
                self.root.after(500, self.check_match)

    def check_match(self):
        idx1, idx2 = self.selected[-2], self.selected[-1]
        if self.cards[idx1] != self.cards[idx2]:
            self.buttons[idx1].config(text=" ")
            self.buttons[idx2].config(text=" ")
        self.selected = []

        if all(button.cget("text") != " " for button in self.buttons):
            messagebox.showinfo("Memory Match", "Congratulations! You've matched all pairs.")

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryMatch(root)
    root.mainloop()
