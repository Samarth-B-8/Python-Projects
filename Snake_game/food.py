from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        # Creating a food which is of the shape circle and has a radius of 10px
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("Blue")
        self.penup()
        self.relocate()
        
    def relocate(self):
        x = randint(-280, +280)
        y = randint(-280, +280)
        self.goto(x=x, y=y)
