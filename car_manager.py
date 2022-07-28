from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        super(CarManager, self).__init__()
        self.all_cars = []

    def create_car(self):
        r = random.randint(1, 6)
        if r == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(400, (random.randint(-25, 25))*10)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(5)

