# Testing the turtle module
from turtle import Turtle, Screen
import turtle as t
import random

tim = Turtle()

########### Challenge 4 - Random Walk ########
colours = [
    "CornflowerBlue",
    "DarkOrchid",
    "IndianRed",
    "DeepSkyBlue",
    "LightSeaGreen",
    "wheat",
    "SlateGray",
    "SeaGreen",
]
directions = [0, 90, 180, 270]
# Each time it progresses by the same distance
# A random direction (90 * some multiple 1-4)
# Different colour
tim.speed("fastest")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(gap):
    for i in range(int(360 / gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap)


draw_spirograph(20)


screen = Screen()
screen.exitonclick()
