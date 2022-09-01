import time
from turtle import Screen
from paddle import Paddle, RightPaddle, LeftPaddle
from ball import Ball
from board import Board


game_is_on = True
screen = Screen()

screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game ")
right_paddle = RightPaddle((350, 0))
left_paddle = LeftPaddle((-350, 0))

my_ball = Ball()
bor = Board()


def end_game():
    global game_is_on
    game_is_on = False


screen.listen()
screen.onkeypress(fun=right_paddle.up, key="Up")
screen.onkeypress(fun=right_paddle.down, key="Down")
screen.onkeypress(fun=left_paddle.up, key="z")
screen.onkeypress(fun=left_paddle.down, key="s")
screen.onkey(fun= end_game, key="Escape")


while game_is_on:
    time.sleep(my_ball.speeding)
    my_ball.move()
    screen.update()
    if my_ball.ycor() in (280, -280):
        my_ball.bounce()
# right bounce with paddle
    if my_ball.distance(right_paddle) < 50 and (330 < my_ball.xcor() < 350):
        my_ball.paddle_bounce()
# left bounce with paddle
    if my_ball.distance(left_paddle) < 50 and (-350 < my_ball.xcor() < -330):
        my_ball.paddle_bounce()
# ball out of edge right
    if my_ball.xcor() > 400:
        my_ball.refresh_ball()
        bor.l_point()
        bor.clear()
        bor.refresh_score()

# ball out of edge left
    if my_ball.xcor() < -400:
        my_ball.refresh_ball()
        bor.r_point()
        bor.clear()
        bor.refresh_score()

