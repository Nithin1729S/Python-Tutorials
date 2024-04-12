from turtle import Turtle,Screen
import random
timmy=Turtle()
timmy.shape("turtle")
colors=["CornflowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
directions=[0,90,180,270]
timmy.width(15)
timmy.speed("fastest")
while True:
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(directions))




screen=Screen()
screen.exitonclick()
