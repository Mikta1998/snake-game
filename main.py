from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

class SnakeGame:
    def __init__(self):
        self.snakes = []

    def initialize_snake(self):
        x = 0
        y = 0
        for i in range(3):
            self.snake = Turtle()
            self.snake.penup()
            self.snake.color("white")
            self.snake.shape("square")
            self.snake.setposition(x, y)
            self.snakes.append(self.snake)
            x -= 20

snake = SnakeGame()
snake.initialize_snake()

game_is_on = True

screen.tracer(0)
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for square in snake.snakes:
        square.forward(20)
















screen.exitonclick()