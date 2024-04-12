import turtle
import random
turtle.colormode(255)   #important




def randomcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r,g,b)
    return random_color





timmy=turtle.Turtle()
timmy.shape("turtle")
directions=[0,90,180,270]
timmy.width(15)
timmy.speed("fastest")
for _ in range(100000):
    timmy.color(randomcolor())
    timmy.forward(30)
    timmy.setheading(random.choice(directions))




screen=turtle.Screen()
screen.exitonclick()
