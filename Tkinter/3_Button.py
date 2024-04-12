from tkinter import *

window=Tk()
window.title("Hi there hello".title())
window.minsize(width=500,height=300)

my_label=Label()
my_label.pack()

my_label["text"]="Click The Button NOW!!!"
my_label["font"]="Ubuntu",34

my_button=Button()
my_button.pack()

my_button["text"]="Click Me"

def button_click():
    new_txt=input.get()
    #my_label.config(text="I GOT CLICKED!!!")
    my_label.config(text=new_txt)

my_button['command']=button_click


#Entry

input=Entry(width=100)
input.pack()

#Text Box
text=Text(height=5,width=30)
text.focus()
text.insert(END,"Enter Something Here")
print(text.get("1.0",END))
text.pack()


#Spin Box
def spinbox_command_used():
    """Prints the value fetched from the spinbox"""
    print(spinbox.get())
spinbox=Spinbox(from_=0,to=5,width=5,command=spinbox_command_used)
spinbox.pack()



#Scale

def scale_value(value):
    print(value)
scale=Scale(from_=0,to=100,command=scale_value)
scale.pack()

#CheckButton

def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
checkbutton=Checkbutton(text="Is On?",
                        variable=checked_state,
                        command=checkbutton_used)

checkbutton.pack()


#RadioButton
def radio_used():
    print(radio_state.get())

radio_state=IntVar()
radiobutton1=Radiobutton(text="Option1",command=radio_used,value=1,variable=radio_state)
radiobutton2=Radiobutton(text="Option2",command=radio_used,value=2,variable=radio_state)
radiobutton2.pack()
radiobutton1.pack()

#ListBox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox=Listbox(height=4)
fruits=["Apple","Banana","Orange","Pear"]
for item in fruits:
    listbox.insert(fruits.index(item),item)
listbox.bind("<<ListboxSelect>>",
             listbox_used)
listbox.pack()








window.mainloop()