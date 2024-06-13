import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman")
        self.root.geometry("400x400")

        self.word_list = ["PYTHON", "JAVA", "HTML", "CSS", "JAVASCRIPT", "PHP", "MYSQL", "RUBY"]
        self.secret_word = random.choice(self.word_list)
        self.guesses_left = 6
        self.guessed_letters = []

        self.word_label = tk.Label(self.root, text=self.hide_word(), font=("Arial", 24))
        self.word_label.pack(pady=20)

        self.guess_label = tk.Label(self.root, text=f"Guesses left: {self.guesses_left}", font=("Arial", 18))
        self.guess_label.pack()

        self.entry = tk.Entry(self.root, font=("Arial", 18))
        self.entry.pack(pady=20)

        self.submit_button = tk.Button(self.root, text="Guess", font=("Arial", 14), command=self.make_guess)
        self.submit_button.pack()

    def hide_word(self):
        return ''.join([letter if letter in self.guessed_letters else '_' for letter in self.secret_word])

    def make_guess(self):
        guess = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                messagebox.showwarning("Duplicate Guess", "You already guessed that letter.")
            elif guess in self.secret_word:
                self.guessed_letters.append(guess)
                self.word_label.config(text=self.hide_word())
            else:
                self.guesses_left -= 1
                self.guess_label.config(text=f"Guesses left: {self.guesses_left}")
        else:
            messagebox.showerror("Invalid Guess", "Please enter a single letter.")

        if '_' not in self.hide_word():
            messagebox.showinfo("Congratulations!", f"You guessed the word '{self.secret_word}'!")
            self.root.destroy()

        if self.guesses_left == 0:
            messagebox.showinfo("Game Over", f"Sorry, you ran out of guesses. The word was '{self.secret_word}'.")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
