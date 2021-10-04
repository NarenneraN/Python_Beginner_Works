from turtle import Turtle
positions=[(0,0), (-20,0), (-40,0)]
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for position in positions:
            new_div = Turtle("square")
            new_div.penup()
            new_div.goto(position)
            # new_div.pendown()
            new_div.color((204, 255, 0))
            self.snake_body.append(new_div)

    def move(self):
        for part in range(len(self.snake_body) - 1, 0, -1):
            prev_x = self.snake_body[part - 1].xcor()
            prev_y = self.snake_body[part - 1].ycor()
            # snake_body[part].penup()
            self.snake_body[part].goto(prev_x, prev_y)

        self.snake_body[0].forward(20)
        self.snake_body[0].right(90)
