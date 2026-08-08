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
