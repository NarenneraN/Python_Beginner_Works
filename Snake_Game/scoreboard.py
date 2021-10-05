from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 320)
        print("sff")
        self.update_score()

    def update_score(self):
        self.write(f"Score :- {self.score}", font=('Courier', 14, 'italic'), align='center')

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()
