import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
from level import Level
screen = Screen()
screen.colormode(255)
screen.tracer(0)
screen.title("Naren's Snake Game Python")
screen.setup(700,700)
screen.bgcolor("black")

level_diff = Level()

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_status = True

while game_status:
    screen.update()
    time.sleep(level_diff.speed)
    snake.move()
    if snake.snake_body[0].distance(food) < 15:
        print("Caught that!")
        food.new_food()
        score.increase()
    if snake.snake_body[0].xcor()>340 or snake.snake_body[0].xcor()<-340 or snake.snake_body[0].ycor()<-340 or snake.snake_body[0].ycor()>340:
        game_status = False
        score.game_over()
screen.exitonclick()
