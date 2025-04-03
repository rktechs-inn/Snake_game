import time
from turtle import Screen

import snake_food
from snake_move import SnakeMove
from score import ScoreBoard#This file have snake creation and move

#Screen setup
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)

#ojects for classes
snake = SnakeMove()
food = snake_food.Food()
user_score = ScoreBoard()

screen.listen()     #screen will take the inputs from keyboard
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

#TODO: Snake starting position and creation is in another class file
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    """detect collision with food using distance() -> distance between 2 turtles"""
    if snake.head.distance(food) < 15:
        # print("Nom")
        food.refresh_food()
        user_score.increase_score()
        snake.extend()
        # user_score.high_score()

    #detect wall collision
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 260 or snake.head.ycor() <= -300:
        user_score.game_over()
        is_game_on = False

    #to detect collision with itself
    for segment in snake.snake_progress[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            user_score.game_over()

screen.exitonclick()
