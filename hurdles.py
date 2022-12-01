import random
from turtle import Turtle
from turtle import *
from player import Player

len_list = []
for i in range(-60, 80):
    i += 1
    len_list.append(i)


blockade = (random.randint, random.randint)

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
screen_y = 500

class Hurdle(Player):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_hurdle()
        self.head = self.segments[0]

    def create_hurdle(self):
        screen_width_len = [()]
        start_point = random.choice(len_list)
        x_position = [start_point, start_point - 10, start_point - 20, start_point - 30,
                      start_point - 40, start_point - 50, start_point - 60]
        hurdle_len = random.randint(2, 7)
        y_cor_start = random.randint(50, 180)
        for segment in range(hurdle_len):
            new_segment = Turtle(shape="square")
            new_segment.color("blue")
            new_segment.shapesize(stretch_wid=-0.5)
            new_segment.speed("fastest")
            new_segment.penup()
            new_segment.goto(x=x_position[segment], y=(screen_y/2 - 10))
            self.segments.append(new_segment)

    def move(self):
        for segments in self.segments:
            segments.setheading(-90)
            segments.forward(5)

    def check_collision(self):
        for segment in self.segments:
            segment_position = segment.position()
            if self.head_player.distance(segment_position) < 10:
                return True

    def left(self):
        if self.head_player.xcor() > -60.00:
            self.head_player.setheading(180)
            print(self.head_player.position())


    def right(self):
        if self.head_player.xcor() < 60.00:
            self.head_player.setheading(0)
            print(self.head_player.position())

    def go_forward(self):
        for segment in self.segments:
            if self.segments[0].ycor() < screen_y/2:
                return True
    def race_over(self):
        if self.head_player.ycor() > 225.00:
            return True

    def restart_game(self):
        return True



            # else: