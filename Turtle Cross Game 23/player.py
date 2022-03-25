from turtle import Turtle

STARTING_POSITION = (0, -230)
MOVE_DISTANCE = 10
FINIS_LINE_Y = 230

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_reached_finish_line(self):
        if (self.ycor() > FINIS_LINE_Y):
            return True
        return False