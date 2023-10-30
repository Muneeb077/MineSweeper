from tkinter import Button, Label, messagebox
import random
import configure
import ctypes, sys

class Cell:
    all = []
    cell_count = configure.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine = False ):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.is_open = False
        self.is_mine_flag = False
        self.x = x
        self.y = y
        Cell.all.append(self)

    def button_object(self,location):
        btn = Button(
            location,
            width = 10,
            height = 4,
        )
        btn.bind('<Button-1>', self.left_click) # mouse functions
        btn.bind('<Button-3>', self.right_click)  # mouse functions
        self.cell_btn_object = btn

    @staticmethod
    def cell_count_label(location):
        lbl = Label(
            location,
            bg="#5D6D7E",
            fg="white",
            text=f"Cells left:{Cell.cell_count}",
            font=("",25)
        )
        Cell.cell_count_label_object = lbl

    def left_click(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surronded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            if Cell.cell_count == configure.MINES_COUNT:
                messagebox.showerror("Error", "Congratulation you have won.")

        self.cell_btn_object.unbind("<Button-1>")
        self.cell_btn_object.unbind("<Button-3>")

    def right_click(self,event):
        if not self.is_mine_flag:
            self.cell_btn_object.configure(bg="orange")
            self.is_mine_flag = True
        else:
            self.cell_btn_object.configure(bg="white")
            self.is_mine_flag = False

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        messagebox.showerror("Error","You clicked on a Mine")
        sys.exit()


    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surronded_cells(self):
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
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surronded_cells:
            if cell.is_mine:
                counter += 1
        return counter

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
       picked_cells = random.sample(Cell.all,configure.MINES_COUNT)
       for picked_cell in picked_cells:
           picked_cell.is_mine = True


    def __repr__(self):
        return f"Cell{self.x},{self.y}"