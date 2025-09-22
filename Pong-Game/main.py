# Importing the necessary libraries and modules
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scoreboard
from time import sleep

# Create and intialize the screen 
screen = Screen()
screen.setup(width=800, height=600)
screen.title("The Pong Game")
screen.bgcolor("Black")
screen.tracer(0)

net = Turtle()
net.color("White")
net.penup()
net.goto(0, -290)
net.seth(90)
for i in range(30):
    net.pendown()
    net.forward(20)
    net.penup()
    net.forward(20)

# Create a new paddle
right_pad = Paddle((350, 0))
left_pad = Paddle((-350, 0))

# Create a ball
ball = Ball()

# Create a Scorecard
scoreCard = Scoreboard()

# Event listeners for the paddle movement
screen.listen()
screen.onkey(fun=right_pad.go_up, key="Up")
screen.onkey(fun=right_pad.go_down, key="Down")
screen.onkey(fun=left_pad.go_up, key='w')
screen.onkey(fun=left_pad.go_down, key='s')


game_is_on = True

while game_is_on:
    sleep(0.1)
    screen.update()
    ball.movement()

    # Detecting the walls and making the ball bounce
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()
    
    # Detecting the paddle and making the ball bounce
    if (ball.xcor() > 320 and ball.distance(right_pad) < 50) or (ball.xcor() < -330 and ball.distance(left_pad) < 50):
        ball.bounce_x()

    # Detection of the ball missing the paddle
    if ball.xcor() > 400:
        ball.reset_movement()
        scoreCard.l_point()

    if ball.xcor() < -400:
        ball.reset_movement()
        scoreCard.r_point()


screen.exitonclick()