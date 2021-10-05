from turtle import Turtle
positions=[(0,0), (-20,0), (-40,0)]
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()

    def create_snake(self):
        for position in positions:
            self.grow_snake(position)

    def grow_snake(self,position):
        new_div = Turtle("square")
        new_div.penup()
        new_div.goto(position)
        # new_div.pendown()
        new_div.color((204, 255, 0))
        self.snake_body.append(new_div)

    def add_new_part(self):
        self.grow_snake(self.snake_body[-1].position())

    def move(self):
        for part in range(len(self.snake_body) - 1, 0, -1):
            prev_x = self.snake_body[part - 1].xcor()
            prev_y = self.snake_body[part - 1].ycor()
            # snake_body[part].penup()
            self.snake_body[part].goto(prev_x, prev_y)
        self.snake_body[0].forward(20)

    def up(self):
        if self.snake_body[0].heading()!=270:
         self.snake_body[0].setheading(90)


    def down(self):
        if self.snake_body[0].heading() != 90:
         self.snake_body[0].setheading(270)

    def right(self):
        if self.snake_body[0].heading() != 180:
         self.snake_body[0].setheading(0)

    def left(self):
        if self.snake_body[0].heading() != 0:
         self.snake_body[0].setheading(180)

