import turtle
import time
win = turtle.Screen()
win.setup(width=800, height=750)
win.bgcolor("black")
#win.bgpic("intro1.png")

win.addshape("intro1.gif")
win.addshape("taurus2.gif")

t = turtle.Turtle()
t.shape("intro1.gif")

#win.delay(10)
time.sleep(20)

t.shape("taurus2.gif")
time.sleep(20)



turtle.done()
