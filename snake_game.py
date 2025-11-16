"""
Snake Game - A complete GUI game using tkinter.
Run with: python snake_game.py

Controls:
- Arrow keys or WASD to move the snake
- R to restart after game over
- Esc to exit

Game Rules:
- Snake starts with 3 segments
- Eat food to grow and increase score
- Don't hit walls or yourself
- Speed increases as your score grows
"""

import tkinter as tk
from collections import deque
import random


class SnakeGame:
    """Main game class managing game logic and rendering."""
    
    # Game constants
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    CELL_SIZE = 20
    GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE  # 32 cells
    GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE  # 24 cells
    
    # Colors
    COLOR_BACKGROUND = "#1a1a1a"
    COLOR_GRID = "#2a2a2a"
    COLOR_SNAKE_HEAD = "#00ff00"
    COLOR_SNAKE_BODY = "#00aa00"
    COLOR_FOOD = "#ff0000"
    COLOR_TEXT = "#ffffff"
    
    # Game states
    STATE_PLAYING = "playing"
    STATE_GAME_OVER = "game_over"
    
    # Directions (dx, dy)
    DIRECTIONS = {
        'up': (0, -1),
        'down': (0, 1),
        'left': (-1, 0),
        'right': (1, 0)
    }
    
    def __init__(self, root):
        """Initialize the game."""
        self.root = root
        self.root.title("Snake Game")
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.root.resizable(False, False)
        self.root.configure(bg=self.COLOR_BACKGROUND)
        
        # Create canvas for drawing
        self.canvas = tk.Canvas(
            root,
            width=self.WINDOW_WIDTH,
            height=self.WINDOW_HEIGHT,
            bg=self.COLOR_BACKGROUND,
            highlightthickness=0
        )
        self.canvas.pack()
        
        # Bind keyboard events
        self.root.bind("<KeyPress>", self.handle_key)
        
        # Initialize game state
        self.reset_game()
        
        # Start game loop
        self.tick()
    
    def reset_game(self):
        """Reset game to initial state."""
        # Snake starts at center with 3 segments moving right
        start_x = self.GRID_WIDTH // 2
        start_y = self.GRID_HEIGHT // 2
        self.snake = deque([
            (start_x, start_y),           # Head
            (start_x - 1, start_y),       # Body
            (start_x - 2, start_y)        # Tail
        ])
        
        self.direction = 'right'
        self.next_direction = 'right'  # Store next direction to prevent immediate reversal
        self.score = 0
        self.state = self.STATE_PLAYING
        
        # Spawn initial food
        self.food = self.spawn_food()
        
        # Game speed: starts at 8 ticks/second, increases every 3 points
        self.base_speed = 100  # milliseconds between ticks
    
    def spawn_food(self):
        """Spawn food at a random empty grid cell."""
        while True:
            x = random.randint(0, self.GRID_WIDTH - 1)
            y = random.randint(0, self.GRID_HEIGHT - 1)
            if (x, y) not in self.snake:
                return (x, y)
    
    def handle_key(self, event):
        """Handle keyboard input."""
        key = event.keysym.lower()
        
        # Game over state: R to restart, Esc to exit
        if self.state == self.STATE_GAME_OVER:
            if key == 'r':
                self.reset_game()
                self.draw()
            elif key == 'Escape':
                self.root.quit()
            return
        
        # Playing state: arrow keys and WASD for direction
        direction_map = {
            'up': 'up', 'w': 'up',
            'down': 'down', 's': 'down',
            'left': 'left', 'a': 'left',
            'right': 'right', 'd': 'right'
        }
        
        if key in direction_map:
            new_direction = direction_map[key]
            # Prevent immediate 180-degree reversal
            if not self.is_opposite_direction(self.direction, new_direction):
                self.next_direction = new_direction
        
        elif key == 'Escape':
            self.root.quit()
    
    def is_opposite_direction(self, current, next_dir):
        """Check if next direction is opposite to current."""
        opposites = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }
        return next_dir == opposites[current]
    
    def tick(self):
        """Game tick: update game logic and redraw."""
        if self.state == self.STATE_PLAYING:
            self.update_game()
        
        self.draw()
        
        # Calculate tick rate: increase speed by 1ms every 3 points
        speed_bonus = (self.score // 3) * 10  # Bonus speed reduction per 3 points
        tick_interval = max(50, self.base_speed - speed_bonus)  # Min 50ms (20 FPS)
        
        self.root.after(tick_interval, self.tick)
    
    def update_game(self):
        """Update game state: move snake, check collisions, etc."""
        # Apply the next direction
        self.direction = self.next_direction
        
        # Calculate new head position
        head_x, head_y = self.snake[0]
        dx, dy = self.DIRECTIONS[self.direction]
        new_head = (head_x + dx, head_y + dy)
        
        # Check wall collision
        if not (0 <= new_head[0] < self.GRID_WIDTH and 0 <= new_head[1] < self.GRID_HEIGHT):
            self.state = self.STATE_GAME_OVER
            return
        
        # Check self collision
        if new_head in self.snake:
            self.state = self.STATE_GAME_OVER
            return
        
        # Add new head
        self.snake.appendleft(new_head)
        
        # Check if food eaten
        if new_head == self.food:
            self.score += 1
            self.food = self.spawn_food()
        else:
            # Remove tail if not eating
            self.snake.pop()
    
    def draw(self):
        """Draw game on canvas."""
        self.canvas.delete("all")
        
        # Draw grid background
        self.draw_grid()
        
        # Draw food
        self.draw_rectangle(self.food[0], self.food[1], self.COLOR_FOOD)
        
        # Draw snake
        for i, (x, y) in enumerate(self.snake):
            if i == 0:
                # Head is a different color
                self.draw_rectangle(x, y, self.COLOR_SNAKE_HEAD)
            else:
                # Body segments
                self.draw_rectangle(x, y, self.COLOR_SNAKE_BODY)
        
        # Draw score
        self.canvas.create_text(
            10, 10,
            text=f"Score: {self.score}",
            fill=self.COLOR_TEXT,
            font=("Arial", 12, "bold"),
            anchor="nw"
        )
        
        # Draw game over message if needed
        if self.state == self.STATE_GAME_OVER:
            self.draw_game_over()
    
    def draw_grid(self):
        """Draw subtle grid background."""
        for x in range(0, self.WINDOW_WIDTH, self.CELL_SIZE):
            self.canvas.create_line(
                x, 0, x, self.WINDOW_HEIGHT,
                fill=self.COLOR_GRID,
                width=1
            )
        
        for y in range(0, self.WINDOW_HEIGHT, self.CELL_SIZE):
            self.canvas.create_line(
                0, y, self.WINDOW_WIDTH, y,
                fill=self.COLOR_GRID,
                width=1
            )
    
    def draw_rectangle(self, grid_x, grid_y, color):
        """Draw a filled rectangle at grid position."""
        x1 = grid_x * self.CELL_SIZE
        y1 = grid_y * self.CELL_SIZE
        x2 = x1 + self.CELL_SIZE - 1
        y2 = y1 + self.CELL_SIZE - 1
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
    
    def draw_game_over(self):
        """Draw game over screen with score and instructions."""
        # Semi-transparent overlay (simulate with dark rectangle)
        self.canvas.create_rectangle(
            0, 0,
            self.WINDOW_WIDTH, self.WINDOW_HEIGHT,
            fill="black", stipple="gray50"
        )
        
        # Game over text
        self.canvas.create_text(
            self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2 - 40,
            text="GAME OVER",
            fill=self.COLOR_TEXT,
            font=("Arial", 32, "bold")
        )
        
        # Final score
        self.canvas.create_text(
            self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2,
            text=f"Final Score: {self.score}",
            fill=self.COLOR_TEXT,
            font=("Arial", 20)
        )
        
        # Instructions
        self.canvas.create_text(
            self.WINDOW_WIDTH // 2, self.WINDOW_HEIGHT // 2 + 50,
            text="Press R to Restart or Esc to Exit",
            fill=self.COLOR_TEXT,
            font=("Arial", 14)
        )


def main():
    """Main entry point."""
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
