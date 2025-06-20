import time
import tkinter as tk
from tkinter import *
from datetime import datetime
from win10toast import ToastNotifier
import winsound
import threading

# Initialize window
window = Tk()
window.geometry("500x500")
window.title('Countdown Timer')
window.config(bg='black')

# Variables
hour = IntVar()
minute = IntVar()
second = IntVar()
check = BooleanVar()
display_var = StringVar(value="00:00:00")
stop_flag = BooleanVar(value=False)
pause_flag = BooleanVar(value=False)

# Format time display
def format_time(h, m, s):
    return f"{h:02d}:{m:02d}:{s:02d}"

# Countdown thread
def countdown():
    def run():
        h = hour.get()
        m = minute.get()
        s = second.get()
        total = h * 3600 + m * 60 + s
        while total >= 0 and not stop_flag.get():
            if not pause_flag.get():
                mins, secs = divmod(total, 60)
                hrs, mins = divmod(mins, 60)
                display_var.set(format_time(hrs, mins, secs))
                time.sleep(1)
                total -= 1
            else:
                time.sleep(0.5)
        if not stop_flag.get():
            if check.get():
                winsound.Beep(440, 1000)
            display_var.set("Time's up!")
            ToastNotifier().show_toast("Notification", "Timer is off", duration=5, threaded=True)
    threading.Thread(target=run, daemon=True).start()

# Start Timer
def start_timer():
    stop_flag.set(False)
    pause_flag.set(False)
    countdown()

# Reset Timer
def reset_timer():
    stop_flag.set(True)
    pause_flag.set(False)
    hour.set(0)
    minute.set(0)
    second.set(0)
    display_var.set("00:00:00")
    pause_button.config(text="Pause")

# Pause / Resume
def toggle_pause():
    if pause_flag.get():
        pause_flag.set(False)
        pause_button.config(text="Pause")
    else:
        pause_flag.set(True)
        pause_button.config(text="Resume")

# Display Time
Label(window, textvariable=display_var, font=("Arial", 40, 'bold'), fg="white", bg="black").pack(pady=30)

# Time input fields in one row
input_frame = Frame(window, bg='black')
input_frame.pack(pady=10)

Entry(input_frame, textvariable=hour, width=5, font=('Arial', 14), justify='center').pack(side=LEFT, padx=5)
Entry(input_frame, textvariable=minute, width=5, font=('Arial', 14), justify='center').pack(side=LEFT, padx=5)
Entry(input_frame, textvariable=second, width=5, font=('Arial', 14), justify='center').pack(side=LEFT, padx=5)

Label(window, text="HH        MM        SS", font=('Arial', 10), fg="white", bg="black").pack()

# Music check
Checkbutton(window, text='Check for music', variable=check, onvalue=True, bg='black', fg='white', selectcolor='black').pack(pady=10)

# Buttons
Button(window, text="Start", command=start_timer, bg='yellow', font=('Arial', 12)).pack(pady=5)

pause_button = Button(window, text="Pause", command=toggle_pause, bg='orange', font=('Arial', 12))
pause_button.pack(pady=5)

Button(window, text="Reset", command=reset_timer, bg='red', fg='white', font=('Arial', 12)).pack(pady=5)

window.mainloop()
