# Users guess the U.S. states on the map, if they guess correctly, the state's name will be written on the map.
# If the user types "exit", the game will end and the states that the user did not guess will be saved in a csv file.

import turtle
import pandas

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")

image = "us_states_map.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
guessed_states = []

while len(guessed_states) < 50:
    if len(guessed_states) == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's state's name?").upper()
    else: 
        answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").upper()

    if answer_state == "EXIT":
        break

    states = data.state.str.upper().to_list()

    if answer_state in states:
        state_data = data[data.state.str.upper() == answer_state]
        guessed_states.append(answer_state)
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(int(state_data.x),int(state_data.y))
        pen.write(answer_state.capitalize())


# state_to_learn.csv

missing_states = {
    "state": [],
    "x": [],
    "y": []
}

for state_name in data.state:
    if state_name.upper() not in guessed_states:
        state_data = data[data.state == state_name]
        missing_states["state"].append(state_name)
        missing_states["x"].append(state_data.x.item())
        missing_states["y"].append(state_data.y.item())

new_data = pandas.DataFrame(missing_states)
new_data.to_csv("state_to_learn.csv", index=False)


