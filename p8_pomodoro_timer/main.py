# Click start button to start the timer
# Click reset button to reset the timer 
# After 25 minutes of working, the timer will change to a 5 minutes break
# After 4 times of working, the timer will change to a 20 minutes break

from tkinter import *
import math

# ----------------------------- CONSTANTS ----------------------------------

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ----------------------------- TIMER RESET --------------------------------

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    global reps
    reps = 0


# ----------------------------- TIMER MECHANISM ----------------------------

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = SHORT_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ----------------------------- COUNTDOWN MECHANISM ------------------------

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        check_marks.config(text=marks)


# ----------------------------- UI SETUP -----------------------------------

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, background="#fff")

title_label = Label(text="Timer", fg=GREEN, background="#fff", font=(FONT_NAME, 32))
title_label.grid(row=0, column=1)

canvas = Canvas(width=300, height=214, background="#fff", highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(150, 107, image=photo)  # x and y are half of the canvas size
timer_text = canvas.create_text(150, 115, text="00:00", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 12), command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 12), command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, background="#fff", font=(FONT_NAME, 15))
check_marks.grid(column=1, row=3)


window.mainloop()