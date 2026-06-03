from turtle import Turtle

FONT = ("Courier", 18, "bold")

### Class to track and display game level ###

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.update_score()

    ### Show current level on screen ###

    def update_score(self):

        self.goto(-240, 270)   ### Top left corner ###

        self.write(f"level: {self.level}", align="center", font=FONT)

    ### Increase level when turtle reaches finish line ###

    def increase_score(self):

        self.level += 1
        self.clear()
        self.update_score()

    ### Show game over message in center ###

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)