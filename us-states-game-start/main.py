import turtle, pandas


def get_answer(score, length):
    answer_state = str(
        screen.textinput(
            title=f"{score}/{length}", prompt="What's another state's name?"
        )
    ).title()
    return answer_state


screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)  # Loading a background image

turtle.shape(img)


def main():
    score = 0
    already_guessed = []
    writer = turtle.Turtle()
    writer.penup()
    writer.hideturtle()
    data = pandas.read_csv("50_states.csv")
    states = data.state.to_list()
    # answer_state = str(
    #     screen.textinput(title="Guess the state", prompt="What's another state's name?")
    # ).capitalize()
    while score < len(data):
        answer_state = get_answer(score, len(data))
        if answer_state.lower() == "q":
            output_data = {"States To Learn": []}
            for state in states:
                if state not in already_guessed:
                    output_data["States To Learn"].append(state)
            df = pandas.DataFrame(output_data)
            df.to_csv("states_to_learn")
            break
        if answer_state in states and answer_state not in already_guessed:
            state_data = data[data.state == answer_state]
            writer.goto((int(state_data.x.iloc[0]), int(state_data.y.iloc[0])))
            writer.write(answer_state)
            already_guessed.append(answer_state)
            score += 1


main()

# def get_mouse_click_cor(x, y):
#     print(x, y)


# turtle.onscreenclick(get_mouse_click_cor)  # Event listener

# turtle.mainloop()  # Keep open
