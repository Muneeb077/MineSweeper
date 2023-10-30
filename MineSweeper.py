# Import required modules and classes from tkinter and other custom modules
from tkinter import *
import configure  # Assuming this module contains configuration settings
import new  # Assuming this module contains utility functions
from unit import Cell  # Assuming this module contains the Cell class

# Create the main tkinter window
root = Tk()
root.configure(bg="lightgrey")  # Set background color
root.geometry(f'{configure.WIDTH}x{configure.HEIGHT}')  # Set window size
root.title("Minesweeper")  # Set the title of the game
root.resizable(True, False)  # Make the window non-resizable

# Create the top frame for the game's title
top_frame = Frame(root, bg="grey",
                  width=configure.WIDTH,
                  height=new.height_prct(15))
top_frame.place(x=0, y=0)

# Create the game title label
game_title = Label(top_frame, bg="grey", fg="black",
                   text="MineSweeper Game",
                   font=('', 40)
                   )
game_title.place(x=new.width_prct(28), y=new.height_prct(0))

# Create the main game board frame
board_frame = Frame(root, bg="#5D6D7E",
                    width=new.width_prct(75),
                    height=new.height_prct(75))
board_frame.place(x=new.width_prct(10), y=new.height_prct(20))

# Create a grid of cells using nested loops
for x in range(configure.GRID_SIZE):
    for y in range(configure.GRID_SIZE):
        c = Cell(x, y)
        c.button_object(board_frame)
        c.cell_btn_object.grid(column=x, row=y)

# Create and place the label to display the cell count
Cell.cell_count_label(top_frame)
Cell.cell_count_label_object.place(
    x=new.width_prct(40),
    y=new.height_prct(8)
)

# Initialize the game with random mines
Cell.random_mines()

# Start the tkinter main loop to run the game
root.mainloop()
