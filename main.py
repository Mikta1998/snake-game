from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()
screen.tracer(0)



class SnakeGame:
    def __init__(self):
        self.body_segments = []

    def initialize_snake(self):
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
        if self.body_segments[0].heading() != 270:
            self.body_segments[0].setheading(90)

    def move_left(self):
        if self.body_segments[0].heading() != 0:
            self.body_segments[0].setheading(180)

    def move_down(self):
        if self.body_segments[0].heading() != 90:
            self.body_segments[0].setheading(270)

    def move_right(self):
        if self.body_segments[0].heading() != 180:
            self.body_segments[0].setheading(0)

    def move(self):
        for segment in range(len(self.body_segments)-1, 0, -1):
            x_cor = self.body_segments[segment - 1].xcor()
            y_cor = self.body_segments[segment - 1].ycor()
            self.body_segments[segment].setposition(x_cor, y_cor)
        self.body_segments[0].forward(20)

snake = SnakeGame()
snake.initialize_snake()

screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()

