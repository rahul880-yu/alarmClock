from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_time):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The set Date is:", date)
        print(now)
        if now == set_alarm_time:
            print("Time to Wake up buddy")
            for _ in range(5):
                winsound.Beep(1000, 1000)  # Beep sound
            break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()
clock.title("Cartoon Alarm Clock")
clock.geometry("400x300")

# Cartoon-style elements
background_color = "lightblue"
font_style = ("Comic Sans MS", 16)
font_style_title = ("Comic Sans MS", 24, "bold")

clock.configure(bg=background_color)

title = Label(clock, text="Cartoon Alarm Clock", fg="blue",
              bg=background_color, font=font_style_title)
title.pack(pady=10)

addTime = Label(clock, text="Hour Min Sec", font=font_style)
addTime.pack(pady=10)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime = Entry(clock, textvariable=hour, bg="pink", font=font_style)
hourTime.pack()
minTime = Entry(clock, textvariable=min, bg="pink", font=font_style)
minTime.pack()
secTime = Entry(clock, textvariable=sec, bg="pink", font=font_style)
secTime.pack()

submit = Button(clock, text="Set Alarm", fg="red",
                font=font_style, command=actual_time)
submit.pack(pady=20)

clock.mainloop()
