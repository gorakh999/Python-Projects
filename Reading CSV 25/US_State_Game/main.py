import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "us_state.gif"
screen.setup(width=725, height=491)
screen.addshape(image)
turtle.shape(image)


data = pd.read_csv("states.csv")
state_list = data.state.to_list()
guess_state = []

while (len(guess_state) < 50):
    inputstr = screen.textinput(f"{len(guess_state)}/50 States Correct", "Enter Name of State : ").title()

    if (inputstr == 'Exit'):
        missed_state = [state for state in state_list if state not in guess_state]
        missing_data = pd.DataFrame(missed_state)
        missing_data.to_csv("Mising_States.csv")
        break

    if (inputstr in state_list):
        guess_state.append(inputstr)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == inputstr]
        t.goto(int(state_data.x), int(state_data.y));
        t.write(inputstr)



