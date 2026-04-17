from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#1A5319"
YELLOW = "#f7f5dd"
FONT = "Courier", "bold"
WORK_MIN = 60
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
reps = 0
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_l.config(text="Timer", fg=GREEN)
    check_l.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 1
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        title_l.config(text="Long break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        title_l.config(text="Short break", fg=PINK)
    else:
        count_down(work_sec)
        title_l.config(text="Work", fg=GREEN)


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 1:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "🗸"
        check_l.config(text=marks)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, highlightthickness=0, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(110, 143, text="00:00", fill="white", font=(FONT, 20))
canvas.grid(column=1, row=1)

title_l = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT, 28))
title_l.grid(column=1, row=0)

start_button = Button(text="start", font=(FONT, 10), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", font=(FONT, 10), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_l = Label(fg=GREEN, bg=YELLOW, font=(FONT, 20))
check_l.grid(column=1, row=4)

window.mainloop()
