from turtle import Turtle



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.current_score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.display_score()


    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.display_score()


    def display_score(self):
        self.write(f"Score: {self.current_score}",
                    move=False,
                    align="center",
                    font=("Arial", 12, "normal"))
