import turtle
from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.f_player_name = turtle.textinput("first player name", "enter your name")
        self.s_player_name = turtle.textinput("second player name", "enter your name")
        self.refresh_score()

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def refresh_score(self):
        self.goto(-100, 230)
        self.write(self.l_score, align="center", font=("Arial", 40, "normal"))
        self.goto(100, 230)
        self.write(self.r_score, align="center", font=("Arial", 40, "normal"))
        self.goto(-300, -270)
        self.write("©Souhail Jamhour", align="center", font=("Arial", 8, "normal"))
        self.goto(-170, 250)
        self.write(self.f_player_name, align="center", font=("Arial", 15, "normal"))
        self.goto(170, 250)
        self.write(self.s_player_name, align="center", font=("Arial", 15, "normal"))
