from turtle import Turtle, Screen

class Ball(Turtle):
    
    # Creating a ball of shape circle and color white
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    # Defining the movement of the ball on the screen
    def movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Defining the bouncing of the ball on the screen
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    # Defining the resetting of the ball after each point
    def reset_movement(self):
        self.goto(0, 0)
        self.bounce_x()