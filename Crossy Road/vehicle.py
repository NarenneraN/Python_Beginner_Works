from turtle import Turtle

class Vehicle():
    def __init__(self):
        super().__init__()
        self.start=[0,-260]
        veh=Turtle()
        veh.color("red")
        veh.penup()
        veh.shape("turtle")
        veh.goto(self.start[0],self.start[1])
        veh.setheading(90)
        self.vehicle=veh

    def up(self):
         self.start[1]+=20
         print(self.start[1])
         self.vehicle.goto(self.start[0], self.start[1])
         self.vehicle.setheading(90)
