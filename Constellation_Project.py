import turtle
import time
import random

win = turtle.Screen()
win.setup(width=800, height=750)


def splashPage():
  t.bgcolor("black")
  t.color("White")
  t.penup()
  t.goto(0, 100)
  t.write("Midterm Project", font=("Arial", 24, "italic"), align="center")
  t.right(90)
  t.forward(100)
  t.write("The Libra Constellation", font=("Arial", 24, "italic"), align="center")
  t.forward(100)
  t.write("Majdi Nagi", font=("Arial", 24, "italic"), align="center")
  sleep(20)



#win.bgpic("intro1.png")
'''
win.addshape("intro1.gif")
win.addshape("taurus2.gif")

t = turtle.Turtle()
turtle.speed(50)
t.shape("intro1.gif")

#win.delay(10)
time.sleep(5)

t.shape("taurus2.gif")
time.sleep(5)

'''
turtle.clearscreen()


t.penup()
t.goto(60, -100)
t.pendown()
t.dot(10)
t.goto(-70, -130)
t.dot(10)
t.penup()
#t.goto(60, -100)
#t.pendown()
t.goto(0, -230)
t.dot(10)
t.pendown()
#t.penup()
t.goto(60, -100)

t.goto(54, -94)
t.dot(10)
t.pendown()
#t.rt(-155)
#t.fd(90)
t.goto(-50,-50)

t.dot(10)
#t.rt(15)
#t.fd(80)
t.goto(-100,-5)
t.dot(10)
#t.lt(8)
#t.fd(70)
t.goto(-150,20)
t.dot(15)
#t.fd(120)
t.goto(-300,100)
t.dot(10)
t.penup()
t.goto(-330,150)
for i in range(25):
    x = random.randrange(-332, -318, 2)
    y = random.randrange(146, 158, 2)
    t.goto(x,y)
    t.dot(2)



t.goto(-95,1)
t.dot(10)
t.pendown()
#t.rt(50)
#t.fd(50)

t.dot(10)
#t.penup()
t.goto(-97,52)
t.dot(10)
t.goto(-99,60)
t.dot(10)
t.pendown()
t.goto(-110,75)
t.dot(7)
t.goto(-135,120)
t.dot(7)
t.goto(-250,200)
t.dot(15)
t.penup()
t.goto(50,50)
t.dot(15)
t.goto(50,70)
t.write("Pleiades 1.6")
t.goto(-210,-10)
t.write("Aldebaran \n\t0.85")
t.goto(-390,150)
t.write("Crab Nebula \n    8.4")
t.goto(-240,210)
t.write("Elnath 1.65")




t.hideturtle()
#t.showturtle()




turtle.done()
splashPage()
