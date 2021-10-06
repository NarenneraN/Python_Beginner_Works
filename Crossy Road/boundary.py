from turtle import Turtle
import time
left_border=[[-390],[-280]]
top_border=[[-390],[280]]
right_border=[[390],[280]]
down_border=[[390],[-280]]
class Boundary():
    def __init__(self):
        super().__init__()
        self.create_boundary()

    def create_boundary(self):

        for i in range(29):
            new_div=Turtle()
            new_div.shape("square")
            new_div.color("white")
            new_div.speed("fastest")
            new_div.penup()
            new_div.goto(left_border[0][i],left_border[1][i])
            # time.sleep(1)
            left_border[0].append(left_border[0][i])  #x-axis remains same
            left_border[1].append(int(left_border[1][i]) + 20) #y axis need change
            print(f"{left_border[0][i]}-->{left_border[1][i]}")

        for i in range(39):
            new_div = Turtle()
            new_div.shape("square")
            new_div.color("white")
            new_div.speed("fastest")
            new_div.penup()
            new_div.goto(top_border[0][i], top_border[1][i])
            top_border[0].append(int(top_border[0][i])+20)  # x-axis remains same
            top_border[1].append(int(top_border[1][i]))  # y axis need change
            print(f"{top_border[0][i]}-->{top_border[1][i]}")

        for i in range(29):
            new_div = Turtle()
            new_div.shape("square")
            new_div.color("white")
            new_div.speed("fastest")
            new_div.penup()
            new_div.goto(right_border[0][i], right_border[1][i])
            right_border[0].append(int(right_border[0][i]))  # x-axis remains same
            right_border[1].append(int(right_border[1][i])-20)  # y axis need change
            print(f"{right_border[0][i]}-->{right_border[1][i]}")

        for i in range(39):
            new_div = Turtle()
            new_div.shape("square")
            new_div.color("white")
            new_div.speed("fastest")
            new_div.penup()
            new_div.goto(down_border[0][i], down_border[1][i])
            down_border[0].append(int(down_border[0][i]) - 20)  # x-axis remains same
            down_border[1].append(int(down_border[1][i]))  # y axis need change
            print(f"{down_border[0][i]}-->{down_border[1][i]}")



