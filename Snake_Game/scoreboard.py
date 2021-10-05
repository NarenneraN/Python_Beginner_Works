from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.goto(0, 320)
        self.write(f"Score :- {self.score}", font=('Courier', 14, 'italic'), align='center')

    def increase(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over", font=('Courier', 80, 'italic'), align='center')
        self.goto(0,-70)
        self.write(f"Score :- {self.score}", font=('Courier', 24, 'italic'), align='center')




