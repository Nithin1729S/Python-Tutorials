from  tkinter import *
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    print(count)
    if count>0:
        window.after(1000,count_down,count-1)



# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

#window.after(1000,lambda x:print(x),"Hello")         #prints hello after 1 sec

count_down(5)





title_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
title_label.grid(column=1,row=0)



canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)   #highlightthickness is used ot remove canvas background
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.create_text(100,130,text='00:00',fill="white",font=(FONT_NAME,35,"bold"))










canvas.grid(column=1,row=1)


start_button=Button(text="Start",highlightthickness=0)
reset_button=Button(text="Reset",highlightthickness=0)

start_button.grid(column=0,row=2)
reset_button.grid(column=2,row=2)

check_marks=Label(text="✔",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)





























window.mainloop()