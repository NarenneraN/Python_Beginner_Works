import time

print("Snake Game")
from turtle import Turtle,Screen
from snake import Snake
screen = Screen()
screen.tracer(0)
screen.colormode(255)
screen.title("Naren's Snake Game Python")
screen.setup(700,700)
screen.bgcolor("black")

snake= Snake()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_status = True
while game_status:
    screen.update()
    time.sleep(0.2)
    snake.move()





screen.exitonclick()
