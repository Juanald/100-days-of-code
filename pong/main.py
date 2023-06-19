from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

lpaddle = Paddle((-350, 0))
rpaddle = Paddle((350, 0))
ball = Ball()
score = Scoreboard()


screen.onkey(rpaddle.goup, "Up")
screen.onkey(rpaddle.godown, "Down")
screen.onkey(lpaddle.goup, "w")
screen.onkey(lpaddle.godown, "s")
screen.listen()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect right paddle collision
    if rpaddle.distance(ball) < 50 and ball.xcor() > 330:
        ball.paddle_reflect()

    # Detect left paddle collision
    elif lpaddle.distance(ball) < 50 and ball.xcor() < -330:
        ball.paddle_reflect()

    # Wall collision
    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.reflect()

    # Paddle scores point
    elif ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
