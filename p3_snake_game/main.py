from turtle import Turtle, Screen
import time 
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)     # need to call update() method to update the screen

# CREATE SNAKE BODY

snake = Snake()

# CREATE FOOD

food = Food()

# CREATE SCOREBOARD

scoreboard = ScoreBoard()

# CONTROL THE SNAKE

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# MOVE THE SNAKE
    
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    
    # DETECT COLLISION WITH WALL
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        # game_is_on = False
        # scoreboard.game_over()
        scoreboard.reset()
        snake.reset()


    # DETECT COLLISION WITH TAIL
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
