from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier",20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.goto(-230, 260)
        self.score = 1
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level {self.score}", align=ALIGNMENT, font=FONT)
        self.score += 1

    def end(self):
        self.goto(0,0)
        self.write("Game over", align=ALIGNMENT, font=FONT)
