# import colorgram
# import turtle

# # t1 = turtle.Turtle()

# colors = colorgram.extract('img1.jpg', 30)

# color_list = []
# for col in colors:
#     r = col.rgb.r
#     g = col.rgb.g
#     b = col.rgb.b
#     new_col = (r, g, b)
#     color_list.append(new_col)


# # t1.color((r, g, b))
# # t1.circle(100)

# # print(first_color.rgb)

# # input()

# print(color_list)

import turtle

t1 = turtle.Turtle()
s1 = turtle.Screen()
turtle.colormode(255)

color_list = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27), (235, 164, 191), (156, 24, 23), (21, 188, 230), (238, 169, 157), (162, 210, 182), (138, 210, 232), (0, 123, 54), (88, 130, 182), (180, 187, 211)]
length_col = len(color_list)

t1.hideturtle()

t1.setheading(225)
t1.penup()
t1.forward(300)
t1.setheading(0)

t1.speed(0)
for i in range(1, 51):
    t1.pendown()
    col = color_list[i % length_col]
    t1.dot(30, col)
    t1.penup()
    t1.forward(50)

    if (i % 10 == 0):

        t1.setheading(90)
        t1.forward(50)
        t1.setheading(180)
        t1.forward(500)
        t1.setheading(0)



s1.exitonclick()