import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

# Constants for game settings
GAME_WIDTH = 400
GAME_HEIGHT = 400
SNAKE_SPEED = 100  # in milliseconds
SPACE_SIZE = 20  # Size of each part of the snake
BODY_PARTS = 3  # Initial length of the snake
SNAKE_COLOR = "green"
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"

# Create the canvas to draw the game
canvas = tk.Canvas(root, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

# Variables to control the snake and food
snake_coords = [(0, 0)] * BODY_PARTS  # Coordinates of the snake
snake_squares = []  # Rectangle objects representing the snake
direction = "down"  # Initial direction of the snake

# Create the snake
for x, y in snake_coords:
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake_squares.append(square)

# Create the food
food_x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
food_y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
food = canvas.create_oval(food_x, food_y, food_x + SPACE_SIZE, food_y + SPACE_SIZE, fill=FOOD_COLOR)

# Update the direction based on key press
def change_direction(new_direction):
    global direction
    if new_direction == "left" and direction != "right":
        direction = "left"
    elif new_direction == "right" and direction != "left":
        direction = "right"
    elif new_direction == "up" and direction != "down":
        direction = "up"
    elif new_direction == "down" and direction != "up":
        direction = "down"

# Move the snake
def move_snake():
    global food, food_x, food_y

    # Get the current coordinates of the snake's head
    x, y = snake_coords[0]

    if direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE
    elif direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE

    # Check if the snake hits the wall
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        game_over()
        return

    # Check if the snake hits itself
    if (x, y) in snake_coords:
        game_over()
        return

    # Move the snake's head
    snake_coords.insert(0, (x, y))  # Insert new head at the front of the list
    new_square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake_squares.insert(0, new_square)  # Insert new rectangle for the head

    # Check if the snake eats the food
    if x == food_x and y == food_y:
        canvas.delete(food)
        place_food()  # Place a new food item
    else:
        # Remove the tail of the snake (last coordinate and rectangle)
        del snake_coords[-1]
        canvas.delete(snake_squares[-1])
        del snake_squares[-1]

    # Move the snake body
    for i in range(len(snake_coords)):
        canvas.coords(snake_squares[i], snake_coords[i][0], snake_coords[i][1], 
                      snake_coords[i][0] + SPACE_SIZE, snake_coords[i][1] + SPACE_SIZE)

    # Schedule the next move
    root.after(SNAKE_SPEED, move_snake)

# Place the food at a random location
def place_food():
    global food_x, food_y, food
    food_x = random.randint(0, int(GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE
    food_y = random.randint(0, int(GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
    food = canvas.create_oval(food_x, food_y, food_x + SPACE_SIZE, food_y + SPACE_SIZE, fill=FOOD_COLOR)

# End the game
def game_over():
    canvas.create_text(GAME_WIDTH // 2, GAME_HEIGHT // 2, text="Game Over", fill="red", font=('Arial', 24))

# Bind the arrow keys to change the snake's direction
root.bind("<Left>", lambda event: change_direction("left"))
root.bind("<Right>", lambda event: change_direction("right"))
root.bind("<Up>", lambda event: change_direction("up"))
root.bind("<Down>", lambda event: change_direction("down"))

# Start moving the snake
move_snake()

# Start the Tkinter event loop
root.mainloop()


