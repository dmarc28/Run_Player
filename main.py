import time
from hurdles import Hurdle
from player import Player
from turtle import *


screen = Screen()
screen.setup(140, 400)
screen.tracer(0)
hurdle = Hurdle()
player = Player()


screen.listen()
screen.onkey(player.left, "Left")
# screen.onkey(forward, "Right")
screen.onkey(player.right, "Right")

hurdle.create_hurdle()
move = 0
game_on = True
while game_on:
    hurdle_new_origin = hurdle.head.xcor()
    screen.delay(0)
    time.sleep(.5)
    screen.update()
    player.head_player.forward(10)
    player.head_player.setheading(90)
    hurdle.move()

    move += 1
    if move % 6 == 0:
        hurdle.create_hurdle()


    # else:






screen.exitonclick()
