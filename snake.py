import random
from turtle import Turtle, Screen

COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270
COLORS = ["blue", "red", "green", "yellow", "white", "orange", ]


class Snake:

    def __init__(self):
        self.screen = Screen()
        self.turtle_segments = []
        self.create_snake()
        self.head = self.turtle_segments[0]

    def create_snake(self):
        self.screen.tracer(0)
        for position in COORDINATES:
            self.add_segment(position)
        self.screen.update()

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.speed(1)
        new_turtle.color(random.choice(COLORS))
        new_turtle.goto(position)
        self.turtle_segments.append(new_turtle)
        # self.turtle_segments[0].shape("turtle")

    def reset_snake(self):
        for segment in self.turtle_segments:
            segment.goto(1000, 1000)
        self.turtle_segments.clear()
        self.create_snake()
        self.head = self.turtle_segments[0]

    def extend(self):
        self.add_segment(self.turtle_segments[-1].position())

    def move(self):
        for seg_index in range(len(self.turtle_segments) - 1, 0, -1):
            new_x = self.turtle_segments[seg_index - 1].xcor()
            new_y = self.turtle_segments[seg_index - 1].ycor()
            self.turtle_segments[seg_index].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
