import time
from turtle import Screen
from player import Player
from Car_Manager import CarManager
from ScoeboardCapstone import Scoreboard

### --------------- UI --------------- ###

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)      
screen.listen()



player = Player()
screen.onkey(player.move, "w")   
car_manager = CarManager()
scoreboard = Scoreboard()

###-----------  game loop --------- ###

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

   

    car_manager.create_car()
    car_manager.move_cars()

    

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_score()

screen.exitonclick()
