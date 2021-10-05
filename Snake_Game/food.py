from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        print("fg")
        self.shape("circle")
        self.circle(10)
        self.penup()
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color((247,68,78))
        # self.circle(10)
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x = random.randrange(-320, 320, 20)
        random_y = random.randrange(-320, 320, 20)
        self.goto(random_x, random_y)


