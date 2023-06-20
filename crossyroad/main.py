import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossy Road")

player = Player()
score = Scoreboard()
carmanager = CarManager()
carmanager.spawn_car()

screen.listen()
screen.onkeypress(player.up, "Up")
screen.onkeypress(player.down, "Down")

game_is_on = True
count = 0
while game_is_on:
    time.sleep(0.1)  # can use this to modify speed
    screen.update()

    # Car spawning up to 20 cars
    if count % 6 == 0 and len(carmanager.cars) < 20:
        carmanager.spawn_car()
    count += 1
    carmanager.move()

    # if player completes the level
    if player.ycor() >= FINISH_LINE_Y:
        player.levelup()
        carmanager.speed_up()
        score.level_up()

    # Collision checking
    if carmanager.is_collision(player):
        score.game_over()
        break

screen.exitonclick()
