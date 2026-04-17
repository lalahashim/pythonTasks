from turtle import *
import random

rafael = Turtle()
colormode(255)
rafael.speed(1000)


def random_color():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    final_color = (r, g, b)
    return final_color


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        rafael.color(random_color())
        rafael.circle(100)
        rafael.setheading(rafael.heading() + size_of_gap)


draw_spirograph(9)

screen = Screen()
screen.exitonclick()
