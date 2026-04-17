from turtle import *
import random

colormode(255)
timothee = Turtle()
timothee.speed("fastest")
timothee.penup()
timothee.hideturtle()

color_list = [
    (218, 173, 125), (159, 181, 190), (134, 73, 53), (50, 103, 154), (118, 81, 92), (179, 142, 152), (162, 104, 151),
    (42, 47, 66), (128, 174, 115), (83, 96, 183), (67, 9, 27), (82, 133, 107), (52, 63, 78), (228, 189, 141),
    (194, 91, 72), (220, 226, 221), (62, 49, 38), (115, 41, 56), (91, 143, 118), (70, 67, 52), (209, 181, 189),
    (181, 185, 210), (209, 183, 178), (89, 55, 47), (183, 201, 179), (172, 199, 204), (41, 73, 83)
]

timothee.setheading(225)
timothee.forward(300)
timothee.setheading(0)
all_dots = 100

for dot_count in range(1, all_dots + 1):
    timothee.dot(20, random.choice(color_list))
    timothee.forward(40)

    if dot_count % 10 == 0:
        timothee.setheading(90)
        timothee.forward(50)
        timothee.setheading(180)
        timothee.forward(400)
        timothee.setheading(0)

screen = Screen()
screen.exitonclick()
