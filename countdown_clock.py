import time
import tkinter as tk
from tkinter import *
from datetime import datetime
from win10toast import ToastNotifier 
import winsound
import threading

# Function to format time
def format_time(h, m, s):
    return f"{h:02d}:{m:02d}:{s:02d}"

# Countdown function (runs in a thread)
def countdown():
    def run():
        h = hour.get()
        m = minute.get()
        s = second.get()
        t = h * 3600 + m * 60 + s
        while t >= 0 and not stop_flag.get():
            mins, secs = divmod(t, 60)
            hrs, mins = divmod(mins, 60)
            display_var.set(format_time(hrs, mins, secs))
            time.sleep(1)
            t -= 1

        if not stop_flag.get():
            if check.get():
                winsound.Beep(440, 1000)  # Beep sound for 1 sec
            display_var.set("Time's up!")
            toast = ToastNotifier()
            toast.show_toast("Notification", "Timer is off", duration=5, threaded=True)
    threading.Thread(target=run).start()

# Reset function
def reset_timer():
    stop_flag.set(True)
    hour.set(0)
    minute.set(0)
    second.set(0)
    display_var.set("00:00:00")

# Create window
window = Tk()
window.geometry("500x500")
window.title('Dhawan Timer')
window.config(bg='black')

# Variables
hour = IntVar()
minute = IntVar()
second = IntVar()
check = BooleanVar()
stop_flag = BooleanVar(value=False)
display_var = StringVar(value="00:00:00")

# Countdown display
Label(window, textvariable=display_var, font=("Arial", 40, 'bold'), fg="white", bg="black").pack(pady=30)

# Time input
Label(window, text="Enter the time in HH:MM:SS", font=('Arial', 12, 'bold'), bg="black", fg="white").pack(pady=10)
Entry(window, textvariable=hour, width=5, font=('Arial', 14), justify='center').pack()
Entry(window, textvariable=minute, width=5, font=('Arial', 14), justify='center').pack()
Entry(window, textvariable=second, width=5, font=('Arial', 14), justify='center').pack()

# Options
Checkbutton(window, text='Check for music', onvalue=True, variable=check, bg='black', fg='white', selectcolor='black').pack(pady=10)

# Buttons
Button(window, text="Start Countdown", command=lambda: [stop_flag.set(False), countdown()], bg='yellow', font=('Arial', 12)).pack(pady=5)
Button(window, text="Reset", command=reset_timer, bg='red', fg='white', font=('Arial', 12)).pack(pady=5)

window.mainloop()