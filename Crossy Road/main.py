print("Naren's Crossy Road 😂")
from turtle import Turtle,Screen
from boundary import Boundary
from vehicle import Vehicle
status=True
screen=Screen()
screen.bgcolor("black")
screen.setup(900,700)
screen.tracer(0)
boundary=Boundary()
vehicle=Vehicle()
screen.listen()
screen.onkey(vehicle.up, "Up")
screen.onkey(vehicle.up, "w")
while status:
    screen.update()

screen.exitonclick()