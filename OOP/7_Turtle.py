from turtle import Turtle,Screen
import random
timmy=Turtle()
timmy.shape("turtle")
colors=["medium blue","green yellow","red","gold","yellow","deep pink","indigo","medium slate blue"]
def draw_shape(sides):
    angle = 360 / sides
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(angle)


for _ in range(3,110):
    timmy.color(random.choice(colors))
    draw_shape(_)




screen=Screen()
screen.exitonclick()

