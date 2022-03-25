import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager


screen = Screen()
screen.setup(width=600, height=500)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

manager = CarManager()
score = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    manager.create_car()
    manager.move_cars()

    # Detect Collision with car
    for car in manager.all_cars:
        if (car.distance(player) < 26):
            score.game_over()
            game_is_on = False

    # Detect when the player reacher on other side
    if player.is_reached_finish_line():
        player.go_to_start()
        score.increase_level()
        manager.level_up()

screen.exitonclick()