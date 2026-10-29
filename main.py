from snake import *
from food import *
from scoreboard import *
from turtle import Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(snake.move_up, "w")
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_right, "d")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        snake.increase_snake_size()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.body_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()