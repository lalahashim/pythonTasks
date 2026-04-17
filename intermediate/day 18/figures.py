from turtle import *
import random

rafael = Turtle()
rafael.shape("turtle")

colors = ["lightsteelblue", "darkolivegreen", "mediumvioletred", "gold", "darkgray", "deeppink", "indianred", "saddlebrown"]


def draw_figure(n):
    for _ in range(n):
        rafael.forward(90)
        rafael.right(360/n)


for shape_number in range(3, 11):
    rafael.color(random.choice(colors))
    draw_figure(shape_number)


screen = Screen()
screen.exitonclick()
