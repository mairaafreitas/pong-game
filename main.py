from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()

score = Scoreboard()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision to the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when r_paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()



    # Detect when l_paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        score.clear()
        score.update_scoreboard()


screen.exitonclick()
