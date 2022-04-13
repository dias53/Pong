import turtle
import winsound
from playsound import playsound

wn = turtle.Screen() #creates a screen
wn.title("Messi vs Ronaldo")
wn.bgcolor("lightgreen")
wn.bgpic("zid.gif")
wn.setup(width=800, height=600)
wn.tracer(0)
playsound('zizou.mp3', 0)
#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of the game itself (set at max)
paddle_a.shape("square")
paddle_a.color("darkred")
paddle_a.shapesize(stretch_wid=5, stretch_len = 1)
paddle_a.penup() #remove lines (lines follow the movement of the object)
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("darkblue")
paddle_b.shapesize(stretch_wid=5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Zidane: 0  Materazzi: 0", align = "center", font=("Courier", 24, "bold"))

#Function
def paddle_a_up():
    y = paddle_a.ycor() #returns the y coordinate
    y += 30 #adds 20 pixels to y coordinate (to move up)
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

#Keyboard binding
wn.listen() #tells to listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #when w is pressed function is called
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#Main game loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx) #makes the ball move
    ball.sety(ball.ycor() + ball.dy)


    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #changes the direction of movement
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound("siu.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Zidane: {}  Materazzi: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "bold"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound("Messi.wav", winsound.SND_ASYNC)
        pen.clear()
        pen.write("Zidane: {}  Materazzi: {}".format(score_a, score_b), align = "center", font=("Courier", 24, "bold"))

    #Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        #above checks if the ball and paddle is touching. +40 and -40 indicate the boundaries of the paddle
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
