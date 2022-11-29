import time
from hurdles import Hurdle
from player import Player
from turtle import *

import random




# def forward():
#     player.setheading(0)
#     # player.forward(1)


screen = Screen()
screen.setup(160, 400)
screen.tracer(0)
hurdle = Hurdle()
player = Player()


screen.listen()
screen.onkey(player.left, "Left")
# screen.onkey(forward, "Right")
screen.onkey(player.right, "Right")

hurdle.create_hurdle()
move = 0

while True:
    hurdle_new_origin = hurdle.head.xcor()
    screen.delay(0)
    time.sleep(.5)
    screen.update()

    player.head_player.forward(10)
    if player.head_player.xcor()<90:
        player.head_player.setheading(90)
        hurdle.move()

        # score.game_over()
        move += 1
        if move % 7 == 0:
            hurdle.create_hurdle()
    elif player.head_player.distance(Hurdle) < 5:
        print("hit a barrier. Game End!!!")
        game_on = False

    # else:






screen.exitonclick()
