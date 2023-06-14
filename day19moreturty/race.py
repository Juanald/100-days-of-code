from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)  # Setup screen
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
).lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
thebois = []

for i in range(len(colors)):
    tim = Turtle("turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-225, y=-100 + 50 * i)  # Sets the turtles
    thebois.append(tim)

raceEnd = False
while not raceEnd:
    for turtle in thebois:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() >= 230:
            raceEnd = True
            color = turtle.pencolor()
            print(f"The {color} turtle won!")
            if user_bet == color:
                print("You guessed right!")
            else:
                print("You guessed wrong!")
            break


screen.exitonclick()
