from turtle import Screen, Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

### Class to control the player (turtle) ###

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("Black")
        self.penup()
        self.setheading(90)      # Face upward
        self.goto(STARTING_POSITION)
        self.go_to_start()

    ### Move the turtle forward ###

    def move(self):

        self.forward(MOVE_DISTANCE)

    ### Send turtle back to starting position ###

    def go_to_start(self):

        self.goto(STARTING_POSITION)

    ### Check if turtle reached the top ###

    def is_at_finish_line(self):

        if self.ycor() > FINISH_LINE_Y:

            return True
        else:
            return False