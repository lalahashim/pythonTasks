from turtle import *
import random

rafael = Turtle()
colormode(255)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    final_color = (r, g, b)
    return final_color


directions = [0, 90, 180, 270]
rafael.speed(20)
rafael.pensize(5)

for _ in range(300):
    rafael.color(random_color())
    rafael.forward(30)
    rafael.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()