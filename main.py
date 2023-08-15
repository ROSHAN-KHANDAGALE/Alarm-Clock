import tkinter as tk
from tkinter import ttk
import time
import winsound
from PIL import Image, ImageTk

def set_alarm():
    alarm_time = entry_alarm_time.get()
    current_time = time.strftime("%H:%M:%S")
    
    while current_time != alarm_time:
        current_time = time.strftime("%H:%M:%S")
        label_current_time.config(text=current_time)
        root.update()
        time.sleep(1)
    
    label_status.config(text="Alarm is ringing!")
    winsound.Beep(1000, 4000)  # Beep sound for 2 seconds

# Create the main application window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry('400x280')
root.iconbitmap('../Alaram-Clock-UI/favicon.ico')

# Load the background image
bg_image = Image.open("background.jpg") 
bg_photo = ImageTk.PhotoImage(bg_image)

# Create a label to hold the background image
background_label = ttk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


# Create and place UI elements
label_title = ttk.Label(root, text="Alarm Clock", font=('Cascadia Mono SemiBold', 22) )
label_title.pack(pady=10)

label_alarm_time = ttk.Label(root, text="Set Alarm (HH:MM:SS)", foreground='red', font=('Cascadia Mono SemiBold', 15))
label_alarm_time.pack(pady=20)

entry_alarm_time = ttk.Entry(root, justify='center', width=50, font=('Cascadia Mono SemiBold', 10))
entry_alarm_time.pack(padx=20)

button_set_alarm = ttk.Button(root, text="Set Alarm", command=set_alarm)
button_set_alarm.pack(pady=10)

label_status = ttk.Label(root, text="", font=("Eras Bold ITC", 12))
label_status.pack(pady=10)

label_current_time = ttk.Label(root, text="", font=("Eras Bold ITC", 12))
label_current_time.pack()

# Start the GUI event loop
root.mainloop()
