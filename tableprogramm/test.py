import tkinter as tk

# Create the main window
root = tk.Tk()


# Function to update window title with the current size
def update_title(event):
    # Get the current window width and height
    width = root.winfo_width()
    height = root.winfo_height()

    # Update the window title to show the size
    root.title(f"{width}x{height}")


# Function to spawn a new label
def spawn_label():
    # Create a new label with some text
    global label_count  # To keep track of where to place new labels
    new_label = tk.Label(root, text=f"Label {label_count}")

    # Place the label in the grid, below the button (row increases with each label)
    new_label.grid(row=label_count, column=0, pady=5)

    label_count += 1


# Bind the configure event to update the title when the window is resized
root.bind('<Configure>', update_title)

# Set an initial size for the window
root.geometry("400x300")

# Keep track of how many labels have been created (for grid placement)
label_count = 1

# Create a button that spawns a label when clicked
spawn_button = tk.Button(root, text="Spawn Label", command=spawn_label)
spawn_button.grid(row=0, column=0, pady=10)

# Run the Tkinter event loop
root.mainloop()
