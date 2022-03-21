import turtle
import random
# t1 = turtle.Turtle()
# s1 = turtle.Screen()


# Challenge 1 : Draw a Square
# for i in range(4):
#     t1.forward(100)
#     t1.right(90)

# t1.sleep(10)


# Challenge 2 : Draw dashed line

# for i in range(10):
#     t1.forward(10)
#     t1.penup()
#     t1.forward(10)

# input()



# Challenge 3 : Draw Different figures
t1 = turtle.Turtle()
s1 = turtle.Screen()

colors = ["light salmon", "orange red", "green", "blue", "black"]

# for i in range(3, 11):
#     angle = 360 // i
#     for j in range(i):
#         t1.color(colors[i%5])
#         t1.forward(100)
#         t1.right(angle)

# t1.forward(100)
turtle.colormode(255)

def pick_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# angle = [0, 90, 180, 270]
t1.speed(0)
# for _ in range(200):
#     col = pick_color()
#     t1.color(col)
#     t1.forward(30)
#     # t1.color(random.choice(colors))
#     t1.setheading(random.choice(angle))    


# Challenge 5

def draw_circle():
    col = pick_color()
    t1.color(col)
    t1.circle(100)
    t1.left(4)

for _ in range(90):
    draw_circle()

input()


