import tkinter as tk
import math

GRAY = "#EEEDDE"
YELLOW = "#E0DDAA"
BLACK = "#203239"
VOID = "#141E27"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

def reset_timer():
    global timer,reps
    window.after_cancel(timer)
    label.config(text="Timer",fg=BLACK)
    canvas.itemconfig(timer_text,text="00:00")
    reps = 0
    check_marks.config(text="")

window = tk.Tk()
window.title("Efe's Pomodoro")
window.config(padx=50, pady=50,bg=GRAY)
canvas = tk.Canvas(width=300, height=300,highlightthickness=0)
Photo = tk.PhotoImage(file="tomato.png")
window.iconphoto(False,Photo)
canvas.create_image(150, 150, image=Photo)
canvas.config(bg=YELLOW)
timer_text = canvas.create_text(150, 160, text="00:00", font=("Ariel", 30, "bold"),fill=GRAY)
canvas.pack()
label = tk.Label(text="Timer", font=(FONT_NAME,30),fg=BLACK,bg=GRAY)
label.place(x=90,y=-50)

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg="red")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg="#F1583F")
    else:
        count_down(work_sec)
        label.config(text="Work", fg="green")














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
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)



starter=tk.Button(width=6,height=1,text="Start",highlightthickness=0,command=start_timer)
starter.place(x=50,y=260)
stoper=tk.Button(width=6,height=1,text="reset",highlightthickness=0,command=reset_timer)
stoper.place(x=200,y=260)
check_marks = tk.Label(fg="green", bg=YELLOW)
check_marks.place(x=110, y=270)











window.mainloop()