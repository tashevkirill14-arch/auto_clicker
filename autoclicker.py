import tkinter as tk
from tkinter import messagebox
import mouse
import keyboard

running = False
delay = 0

def start_clicker():
    global running,delay

    try:
        clicks_per_second = int(entry.get())

        if clicks_per_second <= 0:
            messagebox.showerror("Error", "The speed has to be more than 0")
            return
        
        delay = int(1000 / clicks_per_second)

        messagebox.showinfo("Auto Clicker", "Auto clicker is on. Press ESC to stop")
        running = True

        schedule_click()

    except ValueError:
        messagebox.showerror("Error", "Please enter a correct number of clicks per second")

def schedule_click():
    if running:
        mouse.click()
        root.after(delay, schedule_click)

def exit_app():
    global running

    if running:
        running = False

    messagebox.showinfo("Auto Clicker", "You have stopped the auto clicker")
    root.destroy()

def show_info(event):
    messagebox.showinfo("Info", "This auto clicker will click with the same speed as you enter below")

root = tk.Tk()
root.title("Autoclicker")
root.resizable(False, False)
root.configure(bg="#f74b07")

root.bind('i',show_info)

title_label = tk.Label(
    root,
    text="autoclicker",
    font=("Trebuchet MS",16,"bold"),
    bg="#03e0fe",
    fg="#fe8103"
)
title_label.pack(pady=10)

label = tk.Label(
    root,
    text="Clicks per second",
    font=("Trebuchet MS", 12),
    bg="#e0f7fa",
    fg="#00796b",
)
label.pack(pady=5)

entry = tk.Entry(
    root,
    font=("Arial", 12),
    width=10,
    justify='center'    
)
entry.pack(pady=5)
entry.insert(0, "10")

button_frame = tk.Frame(root, bg="#e0f7fa")
button_frame.pack(side=tk.BOTTOM, pady=(20,30))


start_button = tk.Button(
    button_frame,
    text="start",
    command=start_clicker,
    bg="#4caf50",
    activebackground="#66bb6a",
    fg="white",
    font=("Trebuchet MS",12),
    width=8,
)

start_button.grid(row=0, column=0, padx=10)


exit_button = tk.Button(
    button_frame,
    text="exit",
    command=exit_app,
    bg="#f21a0b",
    activebackground="#ef5350",
    fg="white",
    font=("Trebuchet MS",12),
    width=8,
)
exit_button.grid(row=0, column=1, padx=10)

keyboard.add_hotkey('esc', exit_app)


root.protocol("WM_DELETE_WINDOW", exit_app)

root.mainloop()