sam = turtle.Turtle()
sam.setheading(90) # sam will face up like the red arrow
sam.setheading(180)# sam will face left like the blue one
import turtle
t = turtle.Turtle()
t.penup()
t.goto(0,-180)
t.pendown()
t.circle(180)
t.penup() # draw one hour's tick
t.goto(0,0)
t.setheading(0)
t.forward(150)
t.pendown()
t.forward(30)
t.penup() # draw next tick by repeating
t.goto(0,0)

t.setheading(0)    # 3 o'clock
t.setheading(30)   # 1 o'clock
t.setheading(60)   # 2 o'clock
t.setheading(90)   # 12 o'clock
t.setheading(180)  # 9 o'clock
t.setheading(270)  # 6 o'clock

import datetime
currentMinute = datetime.datetime.now().minute
currentHour = datetime.datetime.now().hour
t.penup()
t.goto(0,0)
t.color("red")
t.pendown()
t.setheading(90)
t.right(currentHour * 360/12)
t.forward(100)
t.penup()
t.goto(0,0)
t.pendown()
t.setheading(90)
t.right(currentMinute * 360/60)
t.forward(150)