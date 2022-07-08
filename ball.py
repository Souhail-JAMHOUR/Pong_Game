from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_step = 10
        self.y_step = 10
        self.speeding = 0.1

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_step *= -1
        self.speeding *= 0.9

    def paddle_bounce(self):
        self.x_step *= -1

    def refresh_ball(self):
        self.speeding = 0.1
        self.home()
        self.x_step *= -1
        self.y_step *= -1
