from turtle import Turtle

class ScoreBar(Turtle):
    def __init__(self):
        super(ScoreBar, self).__init__()
        self.clear()
        self.initial_score = 0
        self.penup()
        self.color("blue")
        self.hideturtle()
        self.clear()
        self.goto(0,160)
        self.Change_Score()

    def increase(self):
        self.clear()
        self.initial_score+=1
        self.Change_Score()

    def Change_Score(self):
        self.write(arg=f"Score: {self.initial_score}", align="center", font=('Arial', 18, 'normal'))

    def game_over(self):
        self.clear()
        self.write(arg=f"Game Over: {self.initial_score}", align="center", font=('Arial', 18, 'normal'))