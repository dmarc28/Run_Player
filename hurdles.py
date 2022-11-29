import random
from turtle import Turtle
from turtle import *
import time

len_list = []
for i in range(-60, 80):
    i += 1
    len_list.append(i)


blockade = (random.randint, random.randint)

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Hurdle:
    def __init__(self):
        self.segments = []
        self.create_hurdle()
        self.head = self.segments[0]

    def create_hurdle(self):
        screen_width_len = [()]
        start_point = random.choice(len_list)
        x_position = [start_point, start_point - 10, start_point - 20, start_point - 30,
                      start_point - 40, start_point - 50, start_point - 60]
        hurdle_len = random.randint(1, 7)
        for segment in range(hurdle_len):
            new_segment = Turtle(shape="square")
            new_segment.color("blue")
            new_segment.shapesize(stretch_wid=-0.5)
            new_segment.speed("fast")
            new_segment.penup()
            new_segment.goto(x=x_position[segment], y=180)
            self.segments.append(new_segment)

    def move(self):
        for segments in self.segments:
            segments.setheading(-90)
            segments.forward(10)

