from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.color("black")
        self.shape("turtle")
        self.tilt(90)
        self.penup()
        self.goto(0, -280)

    def move(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)
