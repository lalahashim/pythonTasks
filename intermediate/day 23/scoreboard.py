from turtle import Turtle
FONT = ("Courier", 10, "normal")
ALIGN = "left"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.hideturtle()
        self.goto(y=280, x=-280)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER!", align=ALIGN, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} ", align=ALIGN, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
