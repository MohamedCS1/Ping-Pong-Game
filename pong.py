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

paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("orange")
paddle2.shapesize(stretch_wid=4 ,stretch_len=1)
paddle2.penup()
paddle2.goto(350 ,0)

while True:
    wind.update()
    
    
    
