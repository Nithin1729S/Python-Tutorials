from turtle import Turtle,Screen
timmy=Turtle()
timmy.shape("turtle")
for _ in range(23):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen=Screen()
screen.exitonclick()

