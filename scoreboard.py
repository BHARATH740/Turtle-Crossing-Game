from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super(ScoreBoard, self).__init__()
        self.score = 1
        self.penup()
        self.color("black")
        self.goto(-380, 270)
        self.write(f"Level : {self.score}", font=("Arial", 16, "bold"))
        self.hideturtle()

    def inc_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level : {self.score}", font=("Arial", 16, "bold"))

    def game_over(self):
        self.clear()
        self.goto(-40, 0)
        self.write(f"Game Over\n Score: {self.score}", font=("Arial", 16, "bold"))
