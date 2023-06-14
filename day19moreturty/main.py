from turtle import Turtle, Screen, reset

tim = Turtle()
screen = Screen()
screen.listen()


def moveForwards():
    tim.forward(10)


def moveBack():
    tim.forward(-10)


def turnClockwise():
    tim.right(10)


def turnCClockwise():
    tim.left(10)


screen.onkeypress(
    key="w", fun=moveForwards
)  # Event listener, on space, execute moveForwards function
screen.onkeypress(moveBack, "s")
screen.onkeypress(turnCClockwise, "a")
screen.onkeypress(turnClockwise, "d")
screen.onkeypress(tim.reset, "c")


screen.exitonclick()
