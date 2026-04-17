import turtle
from turtle import *
import pandas

screen = Screen()
screen.title("Quiz 'U.S. states'")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    guess_state = screen.textinput(f"Guessed states: {len(guessed_states)}/50", "What states are there?").title()

    if guess_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed_states.csv")
        break

    if guess_state in all_states:
        guessed_states.append(guess_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(guess_state)
