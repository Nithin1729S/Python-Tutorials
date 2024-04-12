import tkinter
window=tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)


#Label
my_label=tkinter.Label(text="HI I AM GROOT",font=("Ubuntu",34,"bold"))
my_label.pack()  #puts it in center
#you can use side="left" to put the label in the left and also expand=True to take up all the available space

my_label["text"]='Sorry I am not groot'
my_label.config(text="My first tkinter page".title())  #to change teh label

#Button

def button_clicked():
    print("Yameta Kudasai")





button=tkinter.Button(text="Click Me",command=button_clicked)
button.pack()
























window.mainloop()











