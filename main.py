import time
from turtle import Screen
from player import Player
from cars import Cars
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = Cars(screen, player)
score = Score()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_on = True

while game_on:
    if player.ycor() > 300:
        cars.diff += 1
        player.restart()
        score.update()

    cars.move()
    screen.update()
    time.sleep(0.1)
    if cars.end == 0:
        game_on = cars.end
        score.end()

screen.exitonclick()


