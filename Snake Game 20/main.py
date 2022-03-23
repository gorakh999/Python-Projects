from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=550, height=550)
screen.title("Snake Game")
screen.bgcolor('black')
screen.tracer(0)


snake = Snake()
food= Food()
score = Score()
user_name = screen.textinput(title="Name of Player : ", prompt="Enter your Name : ")

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)


game_on = True

while (game_on):
    screen.update()
    time.sleep(0.1)
    snake.move()


    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        score.increase_score()
        snake.extend()

    
    # Detect collision with walls
    if (snake.head.xcor() >= 273 or snake.head.xcor() <= -273 or snake.head.ycor() >= 273 or snake.head.ycor() <= -273):
        # game_on = False
        # score.game_over()
        # score.bye_user(user_name)
        score.reset()
        snake.reset()



    # Detect collision with snake tail
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 15:
            # game_on = False
            # score.game_over()
            # score.bye_user(user_name)
            score.reset()
            snake.reset()

screen.exitonclick()