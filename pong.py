import turtle
import os

win=turtle.Screen()
win.title("Pong Game")
win.bgcolor("black")
win.setup(width=800,height=600)
win.tracer(0)

#score

score_a=0
score_b=0


#Paddle A

paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#Paddle B

paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball

ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx=0.1
ball.dy=-0.1

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 and Player B: 0", align="center", font=("Times New Roman",24,"normal"))




def paddle_a_up():
	y=paddle_a.ycor()
	y=y+20
	paddle_a.sety(y)

def paddle_a_down():
	y=paddle_a.ycor()
	y=y-20
	paddle_a.sety(y)


def paddle_b_up():
	y=paddle_b.ycor()
	y=y+20
	paddle_b.sety(y)

def paddle_b_down():
	y=paddle_b.ycor()
	y=y-20
	paddle_b.sety(y)

#Keyboard Binding

win.listen()
win.onkeypress(paddle_a_up,"w")
win.onkeypress(paddle_a_down,"s")
win.onkeypress(paddle_b_up,"Up")
win.onkeypress(paddle_b_down,"Down")


while True:
	win.update()

	if score_a>=20:
		pen.goto(0,160)
		pen.write("Game Over!Player A Wins",align="center",font=("Times New Roman",24,"normal"))
		ball.goto(0,0)
		break
	if score_b>=20:
		pen.goto(0,160)
		pen.write("Game Over!Player B Wins",align="center",font=("Times New Roman",24,"normal"))
		ball.goto(0,0)
		break

	#Moving the ball
	ball.setx(ball.xcor()+ball.dx)
	ball.sety(ball.ycor()+ball.dy)								


	#Border Checking
	if ball.ycor()>290:
		ball.sety(290)
		ball.dy=ball.dy*-1
		os.system("aplay bounce.wav&")

	if ball.ycor()<-290:
		ball.sety(-290)
		ball.dy=ball.dy*-1
		os.system("aplay bounce.wav&")

	if ball.xcor()>390:
		ball.goto(0,0)
		ball.dx=ball.dx*-1
		score_a=score_a+1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Times New Roman",24,"normal"))

	if ball.xcor()<-390:
		ball.goto(0,0)
		ball.dx=ball.dx*-1
		score_b=score_b+1
		pen.clear()
		pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center",font=("Times New Roman",24,"normal"))

	if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+40 and ball.ycor()>paddle_b.ycor()-40):
		ball.setx(340)
		ball.dx=ball.dx*-1
		os.system("aplay bounce.wav&")

	if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+40 and ball.ycor()>paddle_a.ycor()-40):
		ball.setx(-340)
		ball.dx=ball.dx*-1
		os.system("aplay bounce.wav&")

win.exitonclick()

	



