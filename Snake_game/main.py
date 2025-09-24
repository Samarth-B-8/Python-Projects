# Snake game

# Importing all the packages
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Setup the output window
screen = Screen()
screen.setup(height=600, width=600)
screen.title("The Snake Game")
screen.bgcolor("Black")
screen.tracer(0)

# Create the snake body
snake = Snake()

# Creating the object for food class
food = Food()

# Creating the object for ScoreBoard
scoreBoard = ScoreBoard()

# Event listeners for controlling the movement of the snake
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

# Displays the status of the game (Gives the condition for the while loop)
is_game_on = True


while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detecting the food collision
    if snake.head.distance(food) < 15:
        food.relocate()
        snake.extend_body()
        scoreBoard.increment()
        # print(scoreBoard.score)
        
    # Detecting the snake if it hits the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreBoard.reset_game()
        snake.reset_snake()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreBoard.reset_game()
            snake.reset_snake()


# Setting the closing condition of the window
screen.exitonclick()
