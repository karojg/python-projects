import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# Get Manual Coordinates
# def get_mouse_click_coordinate(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coordinate)

STATES_COUNT = 50
data = pandas.read_csv("50_states.csv")
all_states = data["state"].to_list()
guessed_states = []


while len(guessed_states) < STATES_COUNT:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{STATES_COUNT} States Correct",
                                    prompt="What's another state's name")

    if answer_state == "Exit" or answer_state is None:
        #     missing_states = []
        #     for state in all_states:
        #         if state not in guessed_states:
        #             missing_states.append(state)
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        # get the coordinate
        state_coordinate = data[data["state"] == answer_state]
        t.goto(int(state_coordinate.x), int(state_coordinate.y))
        t.write(answer_state)

        # using series.item()
        # t.write(state_coordinate.state.item())

turtle.mainloop()

