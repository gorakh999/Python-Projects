from turtle import Turtle, Screen
import random

screen = Screen()

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('pink')
        self.speed(0)
        self.refresh_food()
        

    def refresh_food(self):
        random_x = random.randint(-235, 235)
        random_y = random.randint(-235, 235)
        self.goto(random_x, random_y)

