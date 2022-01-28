from tkinter import *
from tkinter import ttk, messagebox
from queue import PriorityQueue
from collections import deque
import time
import random

GAME_WIDTH = 800
ROWS = 25
font = ("Helvetica", 11)
grid = []
count = 0


# create and define the spot class
class Spot:
    start_point = None
    end_point = None

    def __init__(self, row, col, width, offset, total_rows):
        self.button = Button(canvas, bg='white', relief=RAISED, bd=4, command=lambda: self.click(row, col))
        self.button.place(x=row * width + offset, y=col * width + offset, width=width, height=width)
        self.row = row
        self.col = col
        self.width = width
        self.neighbours = []
        self.total_rows = total_rows

        self.start = False
        self.end = False
        self.barrier = False
        self.clicked = False

    def make_start(self):
        self.button.config(bg='orange')
        self.start = True
        self.clicked = True
        Spot.start_point = (self.row, self.col)

    def make_end(self):
        self.button.config(bg='blue')
        self.end = True
        self.clicked = True
        Spot.end_point = (self.row, self.col)

    def make_barrier(self):
        self.button.config(bg='black')
        self.barrier = True
        self.clicked = True

    def reset(self):
        self.button.config(bg='white')
        self.clicked = False

    def make_path(self):
        self.button.config(bg='yellow')

    def make_open(self):
        self.button.config(bg='green')

    def make_closed(self):
        self.button.config(bg='red')

    def click(self, row, col):
        if not self.clicked:
            if not Spot.start_point:
                self.make_start()
            elif not Spot.end_point:
                self.make_end()
            else:
                self.make_barrier()

        else:
            self.reset()
            if self.start:
                self.start = False
                Spot.start_point = None
            elif self.end:
                self.end = False
                Spot.end_point = None
            else:
                self.barrier = False


def build_maze():
    pass


def start_search():
    pass


def reset_all():
    Spot.start_point = None
    Spot.end_point = None

    for row in grid:
        for spot in row:
            spot.reset()


def make_grid(width, rows):
    grid = []
    offset = 2
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, offset, rows)
            grid[i].append(spot)

    return grid


# creating main window
window = Tk()
window.title("Pathfinder visualisation")
window.resizable(False, False)
window.config(bg="grey")

# creating frame for the user interface
frame = Frame(window, bg="grey", height=800, width=216)
frame.grid(row=0, column=0, padx=5, pady=5)

select_build = StringVar()
select_alg = StringVar()

# creating canvas for the grid
canvas = Canvas(window, bg="white", height=GAME_WIDTH, width=800)
canvas.grid(row=0, column=1, padx=5, pady=5)

# not sure why I need this but I do
window.update()

# centering the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# create dropdown menu to select the maze builder
build_menu = ttk.Combobox(frame,
                          textvariable=select_build,
                          font=font,
                          values=['Random walls', 'Circular maze', 'Carved out maze'])
build_menu.grid(row=0, column=0, padx=5, pady=5)
build_menu.current(0)

# create the scale for obstacle density
obstacle_scale = Scale(frame,
                       from_=10, to=40,
                       orient=HORIZONTAL,
                       label="Wall Density",
                       font=font,
                       length=200,
                       resolution=0.1)
obstacle_scale.grid(row=1, column=0, padx=5, pady=5, sticky=W)

# create the button which builds the maze
build_maze_button = Button(frame,
                           text="Build Maze",
                           command=build_maze,
                           font=("Helvetica", 15),
                           bg="orange",
                           bd=4,
                           relief=RAISED)
build_maze_button.grid(row=2, column=0, padx=5, pady=5)

# create drop-down for search algorithm used
algorithm_menu = ttk.Combobox(frame, textvariable=select_alg,
                              values=['A* Search', 'Breadth-First Search'],
                              font=font)
algorithm_menu.grid(row=3, column=0, padx=5, pady=5)
algorithm_menu.current(0)

# create search speed scale
speed_scale = Scale(frame,
                    from_=10, to=40,
                    orient=HORIZONTAL,
                    label="Search Speed",
                    font=font,
                    length=200)
speed_scale.grid(row=4, column=0, padx=5, pady=5, sticky=W)

# create button to begin selected algorithm
start_button = Button(frame,
                      text="Start Search",
                      command=start_search,
                      font=("Helvetica", 15),
                      bg="green",
                      bd=4,
                      relief=RAISED)
start_button.grid(row=5, column=0, padx=5, pady=5)

# create reset button
reset_button = Button(frame,
                      text="Reset",
                      command=reset_all,
                      font=("Helvetica", 15),
                      bg="light blue",
                      bd=4,
                      relief=RAISED)
reset_button.grid(row=6, column=0, padx=5, pady=5)

# create the grid
grid = make_grid(GAME_WIDTH, ROWS)

# create window
window.mainloop()
