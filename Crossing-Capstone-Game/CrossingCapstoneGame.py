import time
from turtle import Screen
from player import Player
from Car_Manager import CarManager
from ScoeboardCapstone import Scoreboard

### Setup game window ###

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)      ### Turn off animation ###
screen.listen()

### Create game objects ###

player = Player()
screen.onkey(player.move, "w")   # Press W to move forward
car_manager = CarManager()
scoreboard = Scoreboard()

### Main game loop ###

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    ### Create and move cars ###

    car_manager.create_car()
    car_manager.move_cars()

    ### Check collision with cars ###

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    ### Check if player reached the finish line ###

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()