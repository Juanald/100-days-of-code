# Get a list of tuples containing each colour
import colorgram
from turtle import Turtle, Screen
import turtle as t
import random

colors = [
    (233, 239, 246),
    (132, 166, 205),
    (221, 148, 106),
    (32, 42, 61),
    (199, 135, 148),
    (166, 58, 48),
    (141, 184, 162),
    (39, 105, 157),
    (237, 212, 90),
    (150, 59, 66),
    (216, 82, 71),
    (168, 29, 33),
    (235, 165, 157),
    (51, 111, 90),
    (35, 61, 55),
    (156, 33, 31),
    (17, 97, 71),
    (52, 44, 49),
    (230, 161, 166),
    (170, 188, 221),
    (57, 51, 48),
    (184, 103, 113),
    (32, 60, 109),
    (105, 126, 159),
    (175, 200, 188),
    (34, 151, 210),
    (65, 66, 56),
]

tim = Turtle()
tim.hideturtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.setpos(-250, -250)


def paint_line(length):
    for i in range(length):
        tim.pendown()
        color = random.choice(colors)
        tim.color(color)
        tim.dot(20, color)
        tim.penup()
        tim.forward(50)


while tim.ycor() < 250:
    paint_line(10)
    tim.setpos(-250, tim.ycor() + 50)

screen = Screen()
screen.exitonclick()
