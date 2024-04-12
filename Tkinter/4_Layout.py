from tkinter import *

window=Tk()
window.title("TKINTER")
window.minsize(width=500,height=500)
window.config(padx=100,pady=50)

#Label Creation

my_label=Label(text="HI")
my_label['font']="Ubuntu",24
my_label.grid(row=0,column=0)

#button creation
def buttonclick():
    print('I got clicked')
button1=Button(text="Button",command=buttonclick)
button2=Button(text="New Button",command=buttonclick)
button2.grid(row=2,column=2)
button1.grid(row=1,column=3)


#Entry

entry=Entry(width=30)
entry.grid(row=3,column=4)































window.mainloop()

