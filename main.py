from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)  # turn off animation

l_paddle = Paddle(-360, 0)
r_paddle = Paddle(360, 0)

# turtle = Turtle()
# turtle.shape("square")
# turtle.color("white")
# turtle.penup()
# turtle.goto(-360,0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()  # when animation is turned off, must update screen manually.
    ball.move()

    # Detect collision with top or bottom
    if ball.ycor() >= 285 or ball.ycor() < -275:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 30 and ball.xcor() > -360:
        ball.bounce_x()

    # Detect if ball goes out of bounds. Right paddle.
    if ball.xcor() > 420:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()

    # Detect if ball goes out of bounds. Left paddle.
    if ball.xcor() < -420:
        print("out of bounds")
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()
        # game_is_on = False

screen.exitonclick()
