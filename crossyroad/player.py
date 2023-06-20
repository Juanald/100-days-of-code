from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Create turtle
# Create keybindings
# Create reset method
class Player(Turtle):
    def __init__(
        self, shape: str = "turtle", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.goto((self.xcor(), self.ycor() + MOVE_DISTANCE))

    def down(self):
        self.goto((self.xcor(), self.ycor() - MOVE_DISTANCE))

    def levelup(self):
        self.goto(STARTING_POSITION)
