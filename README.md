Project Title: Countdown Clock and Timer

Description:
This project is a simple Countdown Clock and Timer application built using Python's Tkinter GUI library. It allows users to input a specific duration in hours, minutes, and seconds. After starting the countdown, the application will display the time decrementing every second. Once the countdown reaches zero, an optional beep sound is played and a desktop notification is shown.

Features:
- Graphical user interface using Tkinter.
- Input fields for hours, minutes, and seconds.
- Optional audio notification using the winsound module.
- Desktop notification using win10toast.
- Real-time clock display at launch.

Requirements:
- Python 3.x
- Modules:
  - tkinter (usually comes with Python)
  - datetime (standard library)
  - time (standard library)
  - winsound (Windows only)
  - win10toast

How to Run:
1. Ensure Python is installed on your system.
2. Install required modules if not already available:
    **pip install win10toast**
3. Save the script as `countdown_timer.py`.
4. Run the script:

# python countdown_timer.py
Usage Instructions:
1. Launch the application window.
2. Enter the desired countdown time in hours, minutes, and seconds.
3. Optionally, check the "Check for music" box to enable a beep sound at the end.
4. Click the "Set countdown" button to start the timer.
5. When time's up, a notification will appear and sound will play (if enabled).

Notes:
- This application is designed for Windows systems due to use of `winsound` and `win10toast`.
- Ensure that system notifications are enabled to receive the timer alert.

Author:
Dhawanharan Mahalingam (Project: Countdown Timer)

