from sqlite3 import Time
from threading import Timer
from time import sleep, time
import turtle

wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("Black")
wind.setup(800 ,600)
wind.tracer(0)
 
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("green")
paddle1.shapesize(stretch_wid=4 ,stretch_len=1)
paddle1.penup()
paddle1.goto(-350 ,0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0 ,0)
ball.dx = 0.1
ball.dy = 0.1

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("orange")
paddle2.shapesize(stretch_wid=4 ,stretch_len=1)
paddle2.penup()
paddle2.goto(350 ,0)

score1 = 0

score2 = 0

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0 ,260)
score.write("Player one : {} Player two : {}".format(score1 ,score2) ,align="center" ,font=("" ,20 ,"bold"))


def paddle1_move_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_move_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)


def paddle2_move_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_move_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)


wind.listen()
wind.onkeypress(paddle1_move_up ,"Up")
wind.onkeypress(paddle1_move_down ,"Down")
wind.onkeypress(paddle2_move_up ,"w")
wind.onkeypress(paddle2_move_down ,"s")

while True:
    wind.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 :
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() <- 290 :
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390 :
        ball.goto(0 ,0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("Player one : {} Player two : {}".format(score1 ,score2) ,align="center" ,font=("" ,20 ,"bold"))

    
    if ball.xcor() <- 390 :
        ball.goto(0 ,0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("Player one : {} Player two : {}".format(score1 ,score2) ,align="center" ,font=("" ,20 ,"bold"))
    

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40) and (ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40) and (ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1