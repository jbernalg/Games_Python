
import imp
from tkinter import *
import settings
import utils

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


#Run the window
root.mainloop() 
