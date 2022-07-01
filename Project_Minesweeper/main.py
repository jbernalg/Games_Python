
from tkinter import *

root = Tk()
#override the settings of the window
root.configure(bg='black')
root.geometry('800x400')  #size window
root.title('Minesweeper Game')  #title window 
root.resizable(False, False)   #resizable window

top_frame = Frame(
    root,
    bg='red', #change later to black
    width=800,
    height=100
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='lightblue', #change later to black
    width=200,
    height=500
)
left_frame.place(x=0, y=100)


#Run the window
root.mainloop() 
