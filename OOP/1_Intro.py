import turtle
import another_module
# print(another_module.another_variable)

timmy=turtle.Turtle()     #class is in capital case ie class name and turtle is a module name
#timmy is an object
timmy.shape("turtle")
timmy.color("red")

for i in range(4):
    timmy.forward(50)
    timmy.right(90)

my_screen=turtle.Screen()
# print(my_screen.canvheight)
my_screen.exitonclick()


