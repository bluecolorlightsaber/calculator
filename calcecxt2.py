import tkinter as tk
import subprocess

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Game Menu")

        self.frame = tk.Frame(self.root, padx=20, pady=20)
        self.frame.pack()

        # List of games and their commands
        self.games = [
            ("Hangman", "python calcext1.py"),
            ("Snake", "python calcext.py"),
            ("tic tac to", "python calcext3.py"),
            ("Memory match", "python calcext4.py")
        ]
        self.root.bind("<Alt-F7>", lambda event: self.launch_game("python calcext7.py"))
        self.create_game_buttons()

    def create_game_buttons(self):
        for game_name, command in self.games:
            tk.Button(self.frame, text=game_name, padx=20, pady=10, font=("Arial", 14), command=lambda c=command: self.launch_game(c)).pack(fill=tk.X)

    def launch_game(self, command):
        try:
            subprocess.Popen(command.split())
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to launch game: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    menu = MainMenu(root)
    root.mainloop()
