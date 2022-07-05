from tkinter import Button
from turtle import left
import random

class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        #append the object to the Cell.all list
        Cell.all.append(self)


    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=3,
            text= f'{self.x},{self.y}'
        )
        btn.bind('<Button-1>', self.left_click_actions) #left click
        btn.bind('<Button-3>', self.right_click_actions) #right click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        print(event)
        print('I am left clicked')

    def right_click_actions(self, event):
        print(event)
        print('I am right clicked')

    @staticmethod
    def randomize_mines():
        picked_cell = random.sample(
            Cell.all, 9
        )
        print(picked_cell)      

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'

