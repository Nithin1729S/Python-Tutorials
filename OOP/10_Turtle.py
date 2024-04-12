import turtle as t
import random
t.colormode(255)   #important




def randomcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color = (r,g,b)
    return random_color





tim=t.Turtle()
tim.shape("turtle")

tim.speed("fastest")

def draw_spiro(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(randomcolor())
        tim.circle(100)
        current_heading=tim.heading()
        tim.setheading(current_heading+size_of_gap)
#size of gap is like angle here


draw_spiro(1)
screen=t.Screen()
screen.exitonclick()
