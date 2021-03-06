
import imp
from tkinter import *
import settings
import utils
from cell import Cell

root = Tk()
#override the settings of the window
root.configure(bg='black')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')  #size window
root.title('Minesweeper Game')  #title window 
root.resizable(False, False)   #resizable window

top_frame = Frame(
    root,
    bg='red', #change later to black
    width=settings.WIDTH,
    height=utils.height_prct(20)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='red',
    fg='white',
    text='Minesweeper Game',
    font=('', 40)
)

game_title.place(
    x=utils.width_prct(25),
    y=0
)

left_frame = Frame(
    root,
    bg='lightblue', #change later to black
    width=utils.width_prct(25),
    height=utils.height_prct(100) #500
)
left_frame.place(x=0, y=utils.height_prct(20))

center_frame = Frame(
    root,
    bg='green',
    width=utils.width_prct(75),
    height=utils.height_prct(80)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(20)
    )

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

#call the label from the cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()
#Run the window
root.mainloop() 
