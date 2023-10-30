from tkinter import *
import configure
import new
from unit import Cell

root = Tk()
root.configure(bg = "lightgrey") # setting background color
root.geometry(f'{configure.WIDTH}x{configure.HEIGHT}') # size of the tkinter window
root.title("Minesweeper") # The title of the game
root.resizable(False, False) # by this command the window will not be resizeable

top_frame = Frame(root,bg= "grey",
                  width = configure.WIDTH,
                  height = new.height_prct(15))

top_frame.place(x=0,y=0)

game_title = Label(top_frame, bg="grey", fg="black",
                   text = "MineSweeper Game",
                   font = ('', 40)
                   )
game_title.place(x=new.width_prct(32),y=new.height_prct(2))

board_frame = Frame(root, bg= "#5D6D7E",
                    width = new.width_prct(75),
                    height = new.height_prct(75))

board_frame.place(x = new.width_prct(12), y = new.height_prct(20))

for x in range(configure.GRID_SIZE):
    for y in range(configure.GRID_SIZE):
        c = Cell(x,y)
        c.button_object(board_frame)
        c.cell_btn_object.grid(column = x, row = y)

Cell.cell_count_label(top_frame)
Cell.cell_count_label_object.place(
    x = new.width_prct(40),
    y = new.height_prct(10)
)

Cell.random_mines()

root.mainloop()