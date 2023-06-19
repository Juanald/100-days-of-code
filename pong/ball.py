from turtle import Turtle

XVEL = 10
YVEL = 10


class Ball(Turtle):
    def __init__(
        self, shape: str = "circle", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("white")
        self.penup()
        self.xvelocity = XVEL
        self.yvelocity = YVEL
        self.move_speed = 0.1

    def move(self):
        self.goto((self.xcor() + self.xvelocity, self.ycor() + self.yvelocity))

    def reflect(self):
        self.yvelocity *= -1

    def paddle_reflect(self):
        self.xvelocity *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.move_speed = 0.1
        self.goto((0, 0))
        self.xvelocity *= -1
