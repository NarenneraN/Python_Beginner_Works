from turtle import Turtle
import time
class Start(Turtle):
    def __init__(self):
        super().__init__()
        print("naren")
        self.color("white")
        self.hideturtle()

    def countdown(self,num):
        print("came")
        for number in range(num,0,-1):
            print(number)
            self.color("white")
            self.write(f"{number}", font=('Courier', 80, 'italic'), align='center')
            time.sleep(1)
            self.clear()
