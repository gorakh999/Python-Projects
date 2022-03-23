from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_POSITION = 20
UP = 90
DOWN = 270
RIGHT = 180
LEFT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in POSITIONS:
            self.add_segment(i)

    def add_segment(self, position):
        new_seg = Turtle('square')
        new_seg.color('white')
        new_seg.penup()
        new_seg.goto(position)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)

        self.head.forward(MOVE_POSITION)

    def up(self):
        if (self.head.heading() != DOWN):
            self.head.setheading(UP)

    def right(self):
        if (self.head.heading() != RIGHT):
            self.head.setheading(LEFT)

    def down(self):
        if (self.head.heading() != UP):
            self.head.setheading(DOWN)

    def left(self):
        if (self.head.heading() != LEFT):
            self.head.setheading(RIGHT)


