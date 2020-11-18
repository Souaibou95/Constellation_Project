import turtle
import random
from time import sleep

turtle.setup(width=800, height=750)
turtle.speed(30)
turtle.hideturtle()


def splashPage():
  turtle.bgcolor("black")
  turtle.color("White")
  turtle.penup()
  turtle.goto(0, 100)
  turtle.write("Midterm Project", font=("Arial", 24, "italic"), align="center")
  turtle.right(90)
  turtle.forward(100)
  turtle.write("The Taurus Constellation", font=("Arial", 24, "italic"), align="center")
  turtle.forward(100)
  turtle.write("Mamadou Diallo", font=("Arial", 24, "italic"), align="center")
  sleep(20)

def pageTwo():
  turtle.hideturtle()
  turtle.clearscreen()
  turtle.pu()
  turtle.setposition(0,100)
  turtle.pd()
  turtle.bgcolor("black")
  turtle.bgpic("taurus2.gif")
  turtle.update()
  sleep(20)
  turtle.clearscreen()

def pageThree():
  
    turtle.penup()
    turtle.goto(60, -100)
    turtle.pendown()
    turtle.dot(10)
    turtle.goto(-70, -130)
    turtle.dot(10)
    turtle.penup()
    turtle.goto(0, -230)
    turtle.dot(10)
    turtle.pendown()
    turtle.goto(60, -100)
    turtle.goto(54, -94)
    turtle.dot(10)
    turtle.pendown()
    turtle.goto(-50,-50)
    turtle.dot(10)
    turtle.goto(-100,-5)
    turtle.dot(10)
    turtle.goto(-150,20)
    turtle.dot(15)
    turtle.goto(-300,100)
    turtle.dot(10)
    turtle.penup()
    turtle.goto(-330,150)
    for i in range(25):
        x = random.randrange(-332, -318, 2)
        y = random.randrange(146, 158, 2)
        turtle.goto(x,y)
        turtle.dot(2)
    turtle.goto(-95,1)
    turtle.dot(10)
    turtle.pendown()
    turtle.dot(10)
    turtle.goto(-97,52)
    turtle.dot(10)
    turtle.goto(-99,60)
    turtle.dot(10)
    turtle.pendown()
    turtle.goto(-110,75)
    turtle.dot(7)
    turtle.goto(-135,120)
    turtle.dot(7)
    turtle.goto(-250,200)
    turtle.dot(15)
    turtle.penup()
    turtle.goto(50,50)
    turtle.dot(15)
    turtle.goto(50,70)
    turtle.write("Pleiades 1.6")
    turtle.goto(-210,-10)
    turtle.write("Aldebaran \n\t0.85")
    turtle.goto(-390,150)
    turtle.write("Crab Nebula \n    8.4")
    turtle.goto(-240,210)
    turtle.write("Elnath 1.65")
    sleep(30)


def moveToRandomLocation():
  turtle.penup()
  turtle.setpos(random.randint(-400,400) , random.randint(-400,400))
  turtle.pendown()

# this function draws stars 
def drawStar(starSize, starColour):
  turtle.color(starColour)
  turtle.pendown()
  turtle.begin_fill()
  for side in range(5):
 		turtle.left(144)
 		turtle.forward(starSize)
  turtle.end_fill()
  turtle.penup()

def drawGalaxy(numberOfStars):
 	starColours = ["#058396","#0275A6","#827E01", "#eefa46"]
 	moveToRandomLocation()
 	#draw lots of small coloured stars
 	for star in range(numberOfStars):
 		turtle.penup()
 		turtle.left( random.randint(-180,180) )
 		turtle.forward( random.randint(5,20) )
 		turtle.pendown()
 		#draw a small star in a random colour
 		drawStar( 2, random.choice(starColours))


def pageFour():
  turtle.bgcolor("black")
  turtle.color("yellow")
  
  #drowing the stars
  turtle.penup()
  turtle.hideturtle()
  turtle.goto(60, -100)
  drawStar(10, "yellow")
  turtle.goto(-70, -130)
  drawStar(10, "yellow")
  turtle.goto(0, -230)
  drawStar(10, "yellow")
  turtle.goto(-50,-45)
  drawStar(10, "yellow")
  turtle.goto(-100,-5)
  drawStar(10, "yellow")
  turtle.goto(-150,20)
  drawStar(20, "yellow")
  turtle.goto(-210,-10)
  turtle.write("Aldebaran \n\t0.85")
  
  turtle.goto(-300,100)
  drawStar(10, "yellow")
  turtle.goto(-330,150)
  for i in range(25):
        x = random.randrange(-332, -318, 2)
        y = random.randrange(146, 158, 2)
        turtle.goto(x,y)
        turtle.dot(2)
  turtle.goto(-390,150)
  turtle.write("Crab Nebula \n    8.4")
  turtle.goto(-110,75)
  drawStar(10, "yellow")
  turtle.goto(-135,120)
  drawStar(10, "yellow")
  turtle.goto(-250,200)
  drawStar(20, "yellow")
  turtle.goto(-240,210)
  turtle.write("Elnath 1.65")
  turtle.goto(50,50)
  drawStar(20, "yellow")
  turtle.goto(50,70)
  turtle.write("Pleiades 1.6")
  
  for star in range(25):
 	  moveToRandomLocation()
 	  drawStar( random.randint(5,25) , "White")
  
  turtle.speed(1000)
  turtle.update()
  #lines
  turtle.penup()
  turtle.goto(60, -100)
  turtle.pendown()
  turtle.goto(-70, -130)
  turtle.penup()
  turtle.goto(0, -230)
  turtle.pendown()
  turtle.goto(55, -100)
  
  turtle.goto(-50,-45)
  
  turtle.goto(-100,-5)
  
  turtle.goto(-150,20)
  
  turtle.goto(-300,100)
  turtle.penup()
  
  turtle.goto(-100,-5)
  turtle.pendown()
  
  turtle.goto(-110,75)
  turtle.goto(-135,120)
  turtle.goto(-250,200)
  turtle.penup()
  turtle.goto(50,50)
  
  sleep(30)



splashPage()
pageTwo()
pageThree()
pageFour()
