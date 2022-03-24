from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = Screen()
screen.bgcolor('black')
screen.setup(width=750, height=500)
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_on = True
while game_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect Collision on Top and Bottom
    if ball.ycor() > SCREEN_HEIGHT//2 - 20 or ball.ycor() < -(SCREEN_HEIGHT//2 - 20):
        ball.bounce_y()

    # Detect Collision with Paddle
    if (ball.distance(r_paddle) < 50) and (ball.xcor() > (SCREEN_WIDTH // 2 - 20)) or (ball.distance(l_paddle) < 50) and (ball.xcor() < -(SCREEN_WIDTH // 2 - 20)):
        ball.bounce_x()

    # Detect right paddle misses
    if ball.xcor() > SCREEN_WIDTH//2 + 30 :
        scoreboard.l_point()
        ball.reset_position()

    # Detect left paddle misses
    if ball.xcor() < -(SCREEN_WIDTH//2 + 30) :
        scoreboard.r_point()
        ball.reset_position()



screen.exitonclick()