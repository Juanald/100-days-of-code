from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
LEFT = 180


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.moveleftvel = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        car = Turtle()
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.shapesize(stretch_len=2, stretch_wid=1)
        car.goto(280, random.randint(-250, 250))
        car.setheading(LEFT)
        self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(self.moveleftvel)
            if car.xcor() <= -320:
                car.goto((280, car.ycor()))

    def speed_up(self):
        self.moveleftvel += MOVE_INCREMENT

    def is_collision(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True
        return False
