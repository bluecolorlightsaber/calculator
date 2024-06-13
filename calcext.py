import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        self.root.resizable(False, False)
        self.canvas_width = 600
        self.canvas_height = 600
        self.block_size = 20
        self.canvas = tk.Canvas(self.root, bg="black", height=self.canvas_height, width=self.canvas_width)
        self.canvas.pack()
        self.direction = 'Right'
        self.snake = [(60, 60), (60, 80), (60, 100)]
        self.food = None
        self.game_running = True
        self.score = 0
        self.high_score = 0
        self.load_high_score()
        self.create_objects()
        self.root.bind("<KeyPress>", self.change_direction)
        self.move_snake()

    def load_high_score(self):
        try:
            with open("highscore.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

    def save_high_score(self):
        with open("highscore.txt", "w") as file:
            file.write(str(self.high_score))

    def create_objects(self):
        self.canvas.delete(tk.ALL)
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + self.block_size, y + self.block_size, fill="green")
        self.create_food()

    def create_food(self):
        if self.food is None:
            x = random.randint(1, (self.canvas_width // self.block_size) - 1) * self.block_size
            y = random.randint(1, (self.canvas_height // self.block_size) - 1) * self.block_size
            self.food = (x, y)
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + self.block_size, self.food[1] + self.block_size, fill="red")

    def change_direction(self, event):
        key = event.keysym.lower()
        current_direction = self.direction.lower()

        if (key == 'left' and current_direction != 'right') or (key == 'a' and current_direction != 'right'):
            self.direction = 'Left'
        elif (key == 'right' and current_direction != 'left') or (key == 'd' and current_direction != 'left'):
            self.direction = 'Right'
        elif (key == 'up' and current_direction != 'down') or (key == 'w' and current_direction != 'down'):
            self.direction = 'Up'
        elif (key == 'down' and current_direction != 'up') or (key == 's' and current_direction != 'up'):
            self.direction = 'Down'

    def move_snake(self):
        if not self.game_running:
            return

        head_x, head_y = self.snake[0]
        if self.direction == 'Left':
            head_x -= self.block_size
        elif self.direction == 'Right':
            head_x += self.block_size
        elif self.direction == 'Up':
            head_y -= self.block_size
        elif self.direction == 'Down':
            head_y += self.block_size

        # Wrap around the walls
        head_x = head_x % self.canvas_width
        head_y = head_y % self.canvas_height

        new_head = (head_x, head_y)

        # Check if snake hits itself
        if new_head in self.snake[1:]:
            self.game_over()
            return

        self.snake = [new_head] + self.snake[:-1]

        # Check if snake eats the food
        if new_head == self.food:
            self.snake.append(self.snake[-1])
            self.food = None
            self.score += 10
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
            self.create_food()

        self.canvas.delete(tk.ALL)
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x + self.block_size, y + self.block_size, fill="green")
        self.canvas.create_rectangle(self.food[0], self.food[1], self.food[0] + self.block_size, self.food[1] + self.block_size, fill="red")
        
        self.draw_score()
        self.root.after(100, self.move_snake)

    def draw_score(self):
        self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white", anchor="nw")
        self.canvas.create_text(self.canvas_width - 50, 10, text=f"High Score: {self.high_score}", fill="white", anchor="ne")

    def game_over(self):
        self.game_running = False
        self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2 - 30, text="GAME OVER", fill="white", font=("Arial", 24))
        self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2, text=f"Score: {self.score}", fill="white", font=("Arial", 18))
        self.canvas.create_text(self.canvas_width / 2, self.canvas_height / 2 + 30, text="Press Enter to play again", fill="white", font=("Arial", 18))
        self.root.bind("<KeyPress-Return>", self.restart_game)

    def restart_game(self, event):
        self.snake = [(60, 60), (60, 80), (60, 100)]
        self.direction = 'Right'
        self.food = None
        self.score = 0
        self.game_running = True
        self.create_objects()
        self.move_snake()

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
