print("Snake Game")
from turtle import Turtle,Screen

screen=Screen()
screen.colormode(255)
screen.title("Naren's Snake Game Python")
screen.setup(700,700)
screen.bgcolor("black")

positions=[(0,0), (-20,0), (-40,0)]
snake_body=[]
for position in positions:
    new_div = Turtle("square")
    new_div.penup()
    new_div.goto(position)
    new_div.pendown()
    new_div.color((204,255,0))
    snake_body.append(new_div)

screen.exitonclick()
