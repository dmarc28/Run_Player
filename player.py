from turtle import *


class Player:
    def __init__(self):
        self.player = []
        self.create_player()
        self.head_player = self.player[0]


    def create_player(self):
        player = Turtle(shape="turtle")
        player.color("Coral")
        player.speed("fastest")
        player.penup()
        player.goto(x=-0, y=-180)
        player.setheading(90)
        self.player.append(player)

    def left(self):
        if self.head_player.xcor() > -60.00:
            self.head_player.setheading(180)
            print(self.head_player.position())
        # else:

    def right(self):
        if self.head_player.xcor() < 60.00:
            self.head_player.setheading(0)
            print(self.head_player.position())
            # else:

        # player.forward(10)