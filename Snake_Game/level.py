from turtle import Turtle,Screen
screen=Screen()

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.speed=0.1
        self.diff_level=1
        self.level_set()

    def level_set(self):
        while True:
            self.diff_level = screen.numinput("Difficulty of Level", "1.Easy\n2.Medium\n3.Difficult")
            if (self.diff_level == 1 or self.diff_level == 2 or self.diff_level == 3):
                break
            self.color((255,255,255))
            self.write(f"Wrong Input!", font=('Courier', 14, 'italic'), align='center')

        if self.diff_level == 1:
            self.speed *= 1
        elif self.diff_level == 2:
            self.speed *= 0.7
        else:
            self.speed *= 0.4