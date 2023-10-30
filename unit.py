# Import necessary modules and classes from tkinter and other standard libraries
from tkinter import Button, Label, messagebox
import random
import configure
import ctypes, sys

# Define a class to represent individual cells in the Minesweeper game
class Cell:
    # Class-level variables to keep track of all cells, cell count, and the cell count label object
    all = [] # List to store all cell objects
    cell_count = configure.CELL_COUNT # Initial cell count
    cell_count_label_object = None # Label object to display the cell count

    def __init__(self, x, y, is_mine = False ):
        # Constructor to initialize a cell object
        self.is_mine = is_mine # Flag indicating if the cell contains a mine
        self.cell_btn_object = None # Button object representing the cell
        self.is_open = False # Flag indicating if the cell is open
        self.is_mine_flag = False # Flag indicating if the player flagged the cell as a mine
        self.x = x # X-coordinate of the cell
        self.y = y # Y-coordinate of the cell
        Cell.all.append(self) # Add the cell object to the list of all cells

    def button_object(self,location):
        # Create a button object for the cell and bind mouse click events
        btn = Button(
            location,
            width = 8,
            height = 2,
        )
        btn.bind('<Button-1>', self.left_click) # Bind left-click event
        btn.bind('<Button-3>', self.right_click)  # Bind right-click event
        self.cell_btn_object = btn # Store the button object

    @staticmethod
    def cell_count_label(location):
        # Create a label to display the remaining cell count
        lbl = Label(
            location,
            bg="black",
            fg="red",
            text=f"Cells left:{Cell.cell_count}",
            font=("",25)
        )
        Cell.cell_count_label_object = lbl # Store the label object

    # Handle left-click event on the cell
    def left_click(self,event):
        # Check if the cell contains a mine
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                # If no mines are adjacent, recursively reveal surrounding cells
                for cell_obj in self.surronded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # Check if the player has won (all non-mine cells are revealed)
            if Cell.cell_count == configure.MINES_COUNT:
                messagebox.showerror("sucess", "Congratulation you have won.")

        # Unbind mouse click events to prevent further interaction with the cell
        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")

    # Handle right-click event on the cell
    def right_click(self,event):
        # Toggle the flag for marking/unmarking the cell as a potential mine
        if not self.is_mine_flag:
            self.cell_btn_object.configure(bg="orange")
            self.is_mine_flag = True
        else:
            self.cell_btn_object.configure(bg="white")
            self.is_mine_flag = False

    # Handle the case when a mine is clicked, displaying an error message and exiting the game
    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        messagebox.showerror("Error","You clicked on a Mine")
        sys.exit()

    # Find a cell by its X and Y coordinates
    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surronded_cells(self):
        # Get a list of surrounding cells
        cells = [
            self.get_cell_by_axis(self.x-1,self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y+1),
            self.get_cell_by_axis(self.x+1, self.y+1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x, self.y-1)
            ]
        # Remove any None values (cells that are outside the grid)
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        # Count the number of mines in the surrounding cells
        counter = 0
        for cell in self.surronded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    # Show the cell and decrement the cell count
    def show_cell(self):
        if not self.is_open:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text = self.surrounded_cells_mines_length)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text = f"Cells Left: {Cell.cell_count}")

            self.cell_btn_object.configure(bg = "white")

        self.is_open = True

    @staticmethod
    def random_mines():
        # Randomly place mines in the cells
        picked_cells = random.sample(Cell.all,configure.MINES_COUNT)
        for picked_cell in picked_cells:
           picked_cell.is_mine = True


    def __repr__(self):
        # Return a string representation of the cell
        return f"Cell{self.x},{self.y}"