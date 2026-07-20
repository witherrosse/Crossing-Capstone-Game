from turtle import Turtle

FONT = ("Courier", 18, "bold")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("Black")
        self.hideturtle()
        self.penup()
        self.update_score()

    

    def update_score(self):

        ''' Show current level on screen '''

        self.goto(-240, 270)   

        self.write(f"level: {self.level}", align="center", font=FONT)

    

    def increase_score(self):

        ''' Increase level when turtle reaches finish line '''

        self.level += 1
        self.clear()
        self.update_score()


    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
