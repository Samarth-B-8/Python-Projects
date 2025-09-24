from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.score = 0
        self.highscore = 0
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.print_score()
    
    def print_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score}  High Score : {self.highscore} ", align=ALIGNMENT, font=FONT)
        

    def increment(self):
        self.score += 1
        self.clear()
        self.print_score()

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.print_score()
        
    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=-30)
        self.write(arg=f"The Final Score is {self.score}", align=ALIGNMENT, font=FONT)
