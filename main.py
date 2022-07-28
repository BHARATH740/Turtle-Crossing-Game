from turtle import Turtle, Screen
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()
refresh_time = 0.1
screen.listen()
screen.onkeypress(player.move, "Up")
game_is_on = True
while game_is_on:
    time.sleep(refresh_time)
    screen.update()
    if player.ycor() == 300:
        scoreboard.inc_score()
        refresh_time *= 0.9
        player.goto(0, -280)
    car_manager.create_car()
    car_manager.move()
    for car in car_manager.all_cars:
        if car.ycor() == 10:
            if player.distance(car) <= 30:
                game_is_on = False
                scoreboard.game_over()
        else:
            if player.distance(car) <= 25:
                game_is_on = False
                scoreboard.game_over()


screen.exitonclick()
