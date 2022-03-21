from turtle import Turtle, Screen
import random

screen = Screen()
# screen.setup(width=300, height=300)

user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle win will the race ? Type the color : ")
# print(user_bet)

race_on = False
colors = ['red', 'blue', 'green', 'black', 'orange', 'violet']
ypos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-290, y = ypos[i])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while (race_on):
    for item in all_turtles:
        
        if item.xcor() > 290:
            race_on = False

            if (item.pencolor() == user_bet):
                print(f"You won. The {item.pencolor()} color Turtle won the match")
            else:
                print(f"You lost. The {item.pencolor()} color Turtle won the match")

        step = random.randint(4, 12)
        item.forward(step)

screen.exitonclick()