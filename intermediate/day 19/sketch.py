from turtle import *

rafael = Turtle()
screen = Screen()


def move_forwards():
    rafael.forward(10)


def move_backwards():
    rafael.back(10)


def turn_left():
    rafael.left(10)


def turn_right():
    rafael.right(10)


def clear():
    rafael.clear()
    rafael.penup()
    rafael.home()
    rafael.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()