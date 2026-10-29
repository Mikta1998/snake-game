from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.display_score()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def display_score(self):
        self.write(f"Score: {self.score}",
                    move=False,
                    align=ALIGNMENT,
                    font=FONT)
