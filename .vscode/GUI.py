import tkinter as tk

def on_button_click():
    label.config(text="Button Clicked!")

# Create main window
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x200")

# Add a label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=20)

# Add a button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
