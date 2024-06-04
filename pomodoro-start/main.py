from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIME = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(TIME)
    timer.config(text="Timer")
    canvas.itemconfig(time_check, text="00:00")
    checkmark.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    work_secs = WORK_MIN*60
    short_break_secs = SHORT_BREAK_MIN*60
    long_break_secs = LONG_BREAK_MIN*60

    if REPS % 8 == 0:
        count_down(long_break_secs)
        timer.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(short_break_secs)
        timer.config(text=f"Break", fg=YELLOW)
    else:
        count_down(work_secs)
        timer.config(text=f"Working", fg=GREEN)


# --------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = "0" + str(seconds)
    if minutes == 0:
        minutes = "00"
    canvas.itemconfig(time_check, text=f"{minutes}:{seconds}")
    if count > 0:
        global TIME
        TIME = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(REPS / 2)
        for _ in range(work_sessions):
            marks += "✔"
            print(checkmark.cget("text"))
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
# window.minsize(500, 500)
window.config(padx=100, pady=50, bg=PINK)


timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"))
timer.config(highlightthickness=0, bg=PINK, fg=YELLOW)
timer.grid(column=2, row=0, columnspan=2)

canvas = Canvas(window, width=205, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(103, 112, image=tomato_img)
time_check = canvas.create_text(103, 130, text="00:00", fill=YELLOW, font=(FONT_NAME, 28, "bold"))
canvas.grid(column=2, row=3, columnspan=2)

start_button = Button(window, text="Start", font=(FONT_NAME, 8, "bold"))
start_button.config(command=start_timer)
start_button.grid(column=0, row=4, columnspan=2)

reset_button = Button(window, text="Reset", font=(FONT_NAME, 8, "bold"))
reset_button.config(command=reset_timer)
reset_button.grid(column=4, row=4, columnspan=2)

checkmark = Label(window, font=(FONT_NAME, 16))
checkmark.config(bg=PINK, fg=GREEN, highlightthickness=0)
checkmark.grid(column=2, row=5, columnspan=2)

window.mainloop()
