import tkinter as tk
from datetime import datetime
from tkinter import messagebox

def set_alarm():
    alarm_time = entry.get()
    while True:
        now = datetime.now().strftime("%H:%M:%S")
        if now == alarm_time:
            messagebox.showinfo("Alarm", "Wake up!")
            break
        root.update()

def update_time():
    now = datetime.now().strftime("%H:%M:%S")
    label.config(text=now)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Alarm Clock")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack()

label = tk.Label(root, text="")
label.pack()

update_time()
root.mainloop()