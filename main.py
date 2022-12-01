import time
import turtle

from hurdles import Hurdle
from player import Player
from turtle import *


screen = Screen()
screen.setup(140, 500)
screen.tracer(0)
hurdle = Hurdle()



screen.listen()
screen.onkey(hurdle.left, "Left")
screen.onkey(hurdle.right, "Right")
screen.onkey(hurdle.restart_game, "5")

hurdle.create_hurdle()

move = 0
game_on = True
while game_on:
    hurdle_new_origin = hurdle.head.xcor()
    screen.delay(2)
    time.sleep(.1)
    screen.update()
    hurdle.move()
    # hurdle.go_forward()
    if hurdle.go_forward():
        hurdle.head_player.forward(5)
        hurdle.head_player.setheading(90)

    if hurdle.check_collision():
        print("hit a barrier. Game End!!!")
        response = (screen.textinput("Hit a wall! You Lost!",
                                     "Restart? Y or N? :")).lower()
        game_on = False
    move += 1
    if move % 15 == 0:
        hurdle.create_hurdle()

    if hurdle.race_over():
        print("YaY!!! You Finished the race. You Win.!!!")
        response = (screen.textinput("YaY!!! You Win!!!",
                                     "Restart? Y or N:")).lower()
        game_on = False
# response = (screen.textinput("Y or N ", "Do you want to restart? :")).lower()

if "y" in response:
    turtle.clearscreen()
    exec(open("main.py").read())
else:
    exit()














screen.exitonclick()
