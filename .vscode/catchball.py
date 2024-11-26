import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Catch the Ball Game")
root.geometry("400x500")

# Create the canvas to draw on
canvas = tk.Canvas(root, width=400, height=500, bg="lightblue")
canvas.pack()

# Create the paddle (player)
paddle = canvas.create_rectangle(150, 450, 250, 470, fill="blue")

# Create the ball
ball = canvas.create_oval(190, 190, 210, 210, fill="red")

# Variables to control the game
ball_x_speed = random.choice([-3, -2, 2, 3])
ball_y_speed = 3
paddle_speed = 20
score = 0

# Create a label to show the score
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial", 16))
score_label.pack()

# Move the paddle left
def move_paddle_left(event):
    current_position = canvas.coords(paddle)
    if current_position[0] > 0:
        canvas.move(paddle, -paddle_speed, 0)

# Move the paddle right
def move_paddle_right(event):
    current_position = canvas.coords(paddle)
    if current_position[2] < 400:
        canvas.move(paddle, paddle_speed, 0)

# Check if the ball collides with the paddle
def check_collision():
    global score
    ball_pos = canvas.coords(ball)
    paddle_pos = canvas.coords(paddle)

    if ball_pos[3] >= paddle_pos[1] and paddle_pos[0] < ball_pos[2] and ball_pos[0] < paddle_pos[2]:
        return True
    return False

# Update the ball's position
def update_ball():
    global ball_x_speed, ball_y_speed, score
    canvas.move(ball, ball_x_speed, ball_y_speed)
    ball_pos = canvas.coords(ball)

    # Check if the ball hits the wall
    if ball_pos[0] <= 0 or ball_pos[2] >= 400:
        ball_x_speed = -ball_x_speed
    if ball_pos[1] <= 0:
        ball_y_speed = -ball_y_speed

    # Check if the ball hits the paddle
    if check_collision():
        ball_y_speed = -ball_y_speed
        score += 1
        score_label.config(text=f"Score: {score}")

    # Check if the ball hits the bottom of the window
    if ball_pos[3] >= 500:
        canvas.create_text(200, 250, text="Game Over", font=("Arial", 24), fill="red")
        return

    # Continue moving the ball
    root.after(20, update_ball)

# Bind keys to move the paddle
root.bind("<Left>", move_paddle_left)
root.bind("<Right>", move_paddle_right)

# Start the ball movement
update_ball()

# Run the Tkinter event loop
root.mainloop()

