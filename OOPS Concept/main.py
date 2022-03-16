# import turtle

# myturtle = turtle.Turtle()

# screen_size = turtle.Screen()
# myturtle.color("red", "yellow")
# turtle.begin_fill()
# count = 1
# while 1:
#     myturtle.forward(200)
#     myturtle.left(170)
#     if (count == 50):
#         break
#     count += 1
# turtle.end_fill()
# turtle.done()

# screen_size.exitonclick()


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()