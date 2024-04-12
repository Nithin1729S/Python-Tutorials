import turtle
import pandas
screen=turtle.Screen()
screen.title("US States Game")

image="blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

# def get_mouse_click(x,y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click)
data=pandas.read_csv("50_states.csv")

guessed_states=[]
while len(guessed_states)<50:

    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What's another state's name?").title()
    if answer_state=='Exit':
        missing_states=[state for state in data.state.to_list() if state not in guessed_states]
        # for state in data.state.to_list():
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")

        break
    if answer_state in data.state.to_list():
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        #t.write(state_data.state.item())   #item grabs teh first element
        t.write(answer_state)
















#
# turtle.mainloop()


























#screen.exitonclick()