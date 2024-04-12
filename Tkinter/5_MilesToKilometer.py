from tkinter import *
window=Tk()

window.title("Miles to Kilometers Converter")

def button_click():
    miles = miles_input.get()
    kms = round(int(miles) * 1.609,2)
    label4.config(text=kms)




miles_input=Entry()
miles_input.grid(column=1,row=0)


label1=Label(text="Miles")
label1.grid(column=2,row=0)

label2=Label(text='is equal to')
label2.grid(column=0,row=1)

label3=Label(text="Kms")
label3.grid(column=2,rows=1)

label4=Label(text="0")
label4.grid(column=1,row=1)



button=Button(text="Calculate",command=button_click)
button.grid(column=1,row=2)

window.mainloop()

