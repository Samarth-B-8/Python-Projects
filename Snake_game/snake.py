from turtle import Turtle

# Initial position of the body
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]

# Moving distance of the Snake
MOVE_DISTANCE = 20

# The headings of the snake during the turnings
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # function to create the snake body
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segments(position=position)      

    # function to add new segments to the snake body
    def add_segments(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    # Function to extend the snake body
    def extend_body(self):
        self.add_segments(position=self.segments[-1].position())

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(2000,2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # function to control the movement of the complete body
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
