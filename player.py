from turtle import Turtle

SPEED = 20


class Player(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.penup()
        self.shape("turtle")
        self.goto(0, -280)
        self.showturtle()
        self.setheading(90)

    def go_up(self):
        self.setheading(90)
        self.forward(SPEED)

    def go_down(self):
        self.setheading(270)
        self.forward(SPEED)

    def restart(self):
        self.goto(0, -280)
