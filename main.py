import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
screen.tracer(0)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
remaining_states = data.state.to_list()

right_guess = 0
while right_guess < 50:
    screen.update()
    answer = screen.textinput(title=f"{right_guess}/50 States Correct", prompt="What's another state name?").title()
    if answer == "Exit":
        break
    if answer in remaining_states:
        state_x = int(data[data.state == answer].x)
        state_y = int(data[data.state == answer].y)

        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(state_x, state_y)
        t.write(answer, False, "center", ('Arial', 8, 'normal'))

        remaining_states.remove(answer)
        right_guess += 1

states_to_learn = pandas.DataFrame(remaining_states)
states_to_learn.to_csv("states_to_learn.csv")
screen.exitonclick()
