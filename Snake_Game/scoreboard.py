from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("score.txt") as score_file:
         self.high_score=int(score_file.read())
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
        self.goto(0,60)
        self.write(f"Game Over", font=('Courier', 80, 'italic'), align='center')
        self.goto(0,-0)
        self.write(f"Score :- {self.score}", font=('Courier', 24, 'italic'), align='center')

        if self.score>self.high_score:
            self.goto(0,-160)
            self.write(f"Woah! It's High Score 🔥😎", font=('Courier', 24, 'italic'), align='center')
            with open("score.txt","w") as score_file:
                self.high_score = self.score
                score_file.write(str(self.high_score))
        self.goto(0,-60)
        self.write(f"\n\nHigh Score :- {self.high_score}", font=('Courier', 30, 'italic'), align='center')



