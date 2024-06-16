from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Color Changing Clock")

# Define the function to update the time and change color to red at every 5 seconds
def time():
    change_color
    # Get the current time as a string
    current_time = strftime('%H:%M:%S %p')

    #split current_time to get seconds
    sec = (current_time.split())[0].split(":")

    #change color to red every 5 seconds
    if int(sec[-1]) % 5 == 0:
        change_color = "red"
    else:
        change_color = "pink"

    # set foreground to the change_color variable
    var.config(text=current_time, foreground=change_color)

    var.after(1000, time)

var = Label(root, font=("Playground", 100), background= "white")
var.pack(anchor='center')

time()
mainloop()