from turtle import Turtle
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

class Paddle(Turtle):

    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(xpos, ypos)

    def go_up(self):
        if (self.ycor() < (SCREEN_HEIGHT// 2 - 50)):
            self.penup()
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if (self.ycor() > -(SCREEN_HEIGHT// 2 - 50)):
            self.penup()
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)