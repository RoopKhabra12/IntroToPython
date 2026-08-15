#Square
import turtle
t = turtle.Turtle()
t.forward(100)
t.setheading(90)
t.forward(100)
t.setheading(180)
t.forward(100)
t.setheading(270)
t.forward(100)

#Triangle
import turtle
t = turtle.Turtle()
t.forward(100)
t.setheading(120)
t.forward(100)
t.setheading(240)
t.forward(100)

#Snowflake
import turtle

t = turtle.Turtle()
t.pencolor("blue")
t.pensize(5)

# first arm
t.setheading(0)
t.forward(150)
t.backward(30)
t.setheading(60)
t.forward(30)
t.backward(30)
t.setheading(300)
t.forward(30)
t.backward(30)
t.setheading(0)
t.backward(120)

# second arm
t.setheading(60)
t.forward(150)
t.backward(30)
t.setheading(120)
t.forward(30)
t.backward(30)
t.setheading(0)
t.forward(30)
t.backward(30)
t.setheading(60)
t.backward(120)

# third arm
t.setheading(120)
t.forward(150)
t.backward(30)
t.setheading(180)
t.forward(30)
t.backward(30)
t.setheading(60)
t.forward(30)
t.backward(30)
t.setheading(120)
t.backward(120)

# fourth arm
t.setheading(180)
t.forward(150)
t.backward(30)
t.setheading(240)
t.forward(30)
t.backward(30)
t.setheading(120)
t.forward(30)
t.backward(30)
t.setheading(180)
t.backward(120)

# fifth arm
t.setheading(240)
t.forward(150)
t.backward(30)
t.setheading(300)
t.forward(30)
t.backward(30)
t.setheading(180)
t.forward(30)
t.backward(30)
t.setheading(240)
t.backward(120)

# sixth arm
t.setheading(300)
t.forward(150)
t.backward(30)
t.setheading(0)
t.forward(30)
t.backward(30)
t.setheading(240)
t.forward(30)
t.backward(30)
t.setheading(300)
t.backward(120)