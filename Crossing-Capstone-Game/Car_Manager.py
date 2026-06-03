from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

### Class to manage all cars in the game ###

class CarManager:

    def __init__(self):

        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    ### Create a new car randomly (20% chance each frame) ###

    def create_car(self):

        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)   ### Make car shape longer###
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)   # Start from right edge
            self.all_cars.append(new_car)

    ### Move all cars to the left ###

    def move_cars(self):

        for car in self.all_cars:

            car.backward(self.car_speed)

    ### Increase car speed when player levels up ###

    def level_up(self):

        self.car_speed += MOVE_INCREMENT