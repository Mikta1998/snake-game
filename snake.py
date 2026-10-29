from turtle import Turtle

SNAKE_MOVEMENT_SPEED = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.body_segments = []
        self.create_snake()
        self.head = self.body_segments[0]

    def create_snake(self):
        x = 0
        y = 0
        for i in range(3):
            self.body_segment = Turtle()
            self.body_segment.penup()
            self.body_segment.color("white")
            self.body_segment.shape("square")
            self.body_segment.setposition(x, y)
            self.body_segments.append(self.body_segment)
            x -= 20

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for segment in range(len(self.body_segments)-1, 0, -1):
            x_cor = self.body_segments[segment - 1].xcor()
            y_cor = self.body_segments[segment - 1].ycor()
            self.body_segments[segment].setposition(x_cor, y_cor)
        self.head.forward(SNAKE_MOVEMENT_SPEED)