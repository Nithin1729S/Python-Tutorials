import time
from turtle import Turtle,Screen

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  #stops animation  ...animation is stopped until you call update

starting_position=[(0,0),(-20,0),(-40,0)]

segments=[]
for position in starting_position:
    new_segment=Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)







# segment_1=Turtle(shape="square")
# segment_1.color("white")
#
# segment_1=Turtle(shape="square")
# segment_1.color("white")
# segment_1.goto(-20,0)
#
# segment_1=Turtle(shape="square")
# segment_1.color("white")
# segment_1.goto(-40,0)

game_is_on=True

while game_is_on:
    screen.update()  # starts animating  after all segmentshave moved forward
    time.sleep(0.1)  # 1 sec delay after each segment moves

    for seg_num






































screen.exitonclick()