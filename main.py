from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = .5
LONG_BREAK_MIN = 1
REPS = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global REPS
    global LONG_BREAK_MIN
    global WORK_MIN
    global SHORT_BREAK_MIN

    time1 = 0
    REPS += 1

    if REPS <= 8:
        if REPS == 8:
            time1 = LONG_BREAK_MIN * 60
            l1.configure(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
            print("long")

        elif REPS % 2 == 0:
            time1 = SHORT_BREAK_MIN * 60
            l1.configure(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
            print("short")

        else:
            time1 = WORK_MIN * 60
            l1.configure(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
            print("work")

        count_down(time1)
        print(f"==================={REPS}==================================")
    else:
        l1.configure(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))



    # for i in range(1, 8):
    #     print(i)
    #     if i % 2 == 0:
    #         print("short")
    #         time1 = SHORT_BREAK_MIN * 60
    #     else:
    #         time1 = WORK_MIN * 60
    #         print("work")
    #
    #     value1 = count_down(time1)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    print(count)
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = "0" + str(count_sec)

    if count_min < 10:
        count_min = "0" + str(count_min)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        window.after(100, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
# window.config(height=100, width=112)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=205, height=228, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(104, 114, image=tomato_img)
# canvas.create_text(104, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
timer_text = canvas.create_text(104, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

l1 = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
l1.grid(row=0, column=1)

l2 = Label(text="✔ ✔ ✔ ✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"), pady=10)
l2.grid(row=3, column=1, sticky="S")

b1 = Button(text="Start", highlightthickness=0, padx=15, command=start_timer)
b1.grid(row=2, column=0)

b2 = Button(text="Reset", highlightthickness=0, padx=12)
b2.grid(row=2, column=2)

# count_down(5)


window.mainloop()
