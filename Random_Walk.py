import random
from turtle import Turtle, Screen

timmy = Turtle()

timmy.pensize(15)
timmy.speed("fastest")

for _ in range(500):
    timmy.color(random.choice(["red", "blue", "green", "yellow"]))
    timmy.forward(30)
    timmy.right(random.choice([0, 90, 180, 270]))

screen = Screen()
screen.exitonclick()
