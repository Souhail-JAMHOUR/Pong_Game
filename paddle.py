from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")


    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            position = (self.xcor(),new_y)
            self.goto(position)

    def down(self):
        if self.ycor() > -230:
            new_y = self.ycor() - 20
            position = (self.xcor(), new_y)
            self.goto(position)

class RightPaddle(Paddle):
    def __init__(self, position):
        super().__init__()
        self.goto(position)


class LeftPaddle(Paddle):
    def __init__(self, position):
        super().__init__()
        self.goto(position)
