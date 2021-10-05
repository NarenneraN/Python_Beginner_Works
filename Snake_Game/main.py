import time
from turtle import Screen
from snake import Snake
from food import Food
screen = Screen()

# while True:
#  diff_level=turtle.numinput("Difficulty of Level","1.Easy\n2.Medium\n3.Difficult")
#  if (diff_level==1 or diff_level==2 or diff_level==3):
#      break
#  turtle.write("Wrong Input!")

screen.tracer(0)
screen.colormode(255)
screen.title("Naren's Snake Game Python")
screen.setup(700,700)
screen.bgcolor("black")

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_status = True
while game_status:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake_body[0].distance(food) < 15:
        print("Caught that!")
        food.new_food()
screen.exitonclick()
