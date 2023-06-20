from turtle import Turtle

FONT = ("Courier", 24, "normal")
GAMEOVERFONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-200, 250)
        self.score = 0
        self.level_up()

    def level_up(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)
        self.score += 1

    def game_over(self):
        self.clear()
        self.goto(0, 250)
        self.write(
            f"Game Over! You survived {self.score} rounds!",
            align="center",
            font=GAMEOVERFONT,
        )
