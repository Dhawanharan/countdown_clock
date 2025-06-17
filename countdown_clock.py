import time
import tkinter as tk
from tkinter import *
from datetime import datetime
from win10toast import ToastNotifier 
import winsound

#creating a new window
window = Tk()
window.geometry("600x600")      # size of the window
window.title('Dhawan')          # title of the window
Label(window, text= "Countdown Clock and Timer", font=("Arial", 20)).pack(pady=20)

#to print current time
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
Label(window,text=current_time).pack()

check=tk.BooleanVar()   #check boolean type
hour = tk.IntVar()      #check count is int type
minute = tk.IntVar()
second = tk.IntVar()

#defining the function to create the countdown clock
def countdown():
    h = hour.get()
    m = minute.get()
    s = second.get()
    t = h * 3600 + m * 60 + s
    while t:
        mins, secs = divmod(t, 60)
        display = ('{:02d}:{:02d}'.format(mins, secs))
        time.sleep(1)
        t -= 1
        Label(window, text = display).pack()
    
    if (check.get()==True):
        winsound.Beep(440, 1000)    # Beep sound for 1 second
        
    Label(window, text = "Time's up!", font=('bold', 20)).place(x=250, y=440)
    
    #display notification
    toast = ToastNotifier()
    toast.show_toast("Notification","Timer is off", duration = 20, icon_path= NONE, threaded=True)  #show toast
     
Label(window, text="Enter the time in HH:MM:SS ", font=('bold')).pack()
Entry(window, textvariable=hour, width=30).pack()
Entry(window, textvariable=minute, width=30).pack()
Entry(window, textvariable=second, width=30).pack() 

Checkbutton(text='Check for music', onvalue =True, variable=check).pack()
Button(window, text="Set countdown", command = countdown, bg= 'yellow').pack()
window.update()
window.mainloop()

