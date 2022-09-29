from random import randint, choice
from turtle import Turtle

COLORS = ["green", "purple", "red", "orange"]
SPEED = [5, 20]


class Cars:
    def __init__(self, sc, pl):
        self.screen = sc
        self.player = pl
        self.cars = []
        self.diff = 5
        self.flag = 0
        self.end = True

        self.generate()

    def create(self):
        new_car = Turtle(visible=False, shape="square")
        new_car.shapesize(stretch_len=2)
        new_car.setheading(180)
        new_car.penup()
        new_car.color(choice(COLORS))
        new_car.goto(300, randint(-250, 270))
        new_car.showturtle()

        self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.forward(randint(SPEED[0], SPEED[1]))
            if car.distance(self.player.pos()) < 20:
                self.end = False

            if car.xcor() < -320:
                self.cars.remove(car)
        if self.flag % 11 == 0:
            self.generate()
        self.flag += 1

    def generate(self):
        x = 0
        while x < self.diff:
            self.create()
            x += 1


