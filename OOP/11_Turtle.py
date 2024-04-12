from turtle import Turtle,Screen
tim=Turtle()
screen=Screen()

def move_forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space",fun=move_forward)    #dont put () after the function coz you are passing it as a argument into another function






















































screen.exitonclick()