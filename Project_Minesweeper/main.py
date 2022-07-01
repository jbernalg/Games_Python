
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
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

#Run the window
root.mainloop() 
