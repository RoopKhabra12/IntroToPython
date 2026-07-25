#Review
##import turtle
##t = turtle.Turtle() # creating a turtle named 't'
##t.pensize(4)
##t.color("yellow") # this will be the fill colour
##t.pencolor("black") # this will be the pen colour
##t.begin_fill() # remember begin_fill before and end_fill after
##t.circle(100)
##t.end_fill()
##t.color("black")
##t.penup()
##t.goto(-50,80) # we are going 50 steps left of center, 80 up
##t.begin_fill()
##t.circle(20)
##t.end_fill()
##t.goto(50,80) # this is 50 steps right of center, 80 up
##t.begin_fill()
##t.circle(20)
##t.end_fill()
##t.goto(0,40)
##t.color("pink")
##t.begin_fill()
##t.circle(10)
### Left cheek
##t.penup()
##t.goto(-70,40)
##t.color("pink")
##t.begin_fill()
##t.circle(8)
##t.end_fill()
### Right cheek
##t.penup()
##t.goto(55,40)
##t.begin_fill()
##t.circle(8)
##t.end_fill()
import turtle
tina = turtle.Turtle()
tina.color("green") # tina is a green turtle
jamie = turtle.Turtle()
jamie.color("blue") # jamie is a blue turtle
omar = turtle.Turtle()
omar.color("red") # omar is a red turtle
tina.forward(300) # tina will move first
jamie.forward(200) # then jamie will move
omar.forward(100) # then omar will move

import turtle
tina = turtle.Turtle()
tina.color("green")
jamie = turtle.Turtle()
jamie.color("blue")
omar = turtle.Turtle()
omar.color("red")

# Tina draws a triangle
for i in range(3):
    tina.forward(100)
    tina.left(120)

# Jamie draws a circle
jamie.penup()
jamie.goto(150, 0)
jamie.pendown()
jamie.circle(50)

# Omar draws a square
omar.penup()
omar.goto(-150, 0)
omar.pendown()

for i in range(4):
    omar.forward(100)
    omar.left(90)

turtle.done()

import turtle

tina = turtle.Turtle()
jamie = turtle.Turtle()
omar = turtle.Turtle()

tina.color("green")
jamie.color("blue")
omar.color("red")

# Different shapes
tina.shape("turtle")
jamie.shape("circle")
omar.shape("square")

# Different speeds
tina.speed(1)
jamie.speed(5)
omar.speed(0)

# Tina disappears
tina.hideturtle()

# Jamie stamps herself
jamie.stamp()

# Omar moves
omar.forward(150)

turtle.done()

#Q1,2,&3
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()

turtles = [t1, t2, t3, t4, t5, t6]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

x = -250

for i in range(6):
    turtles[i].shape("turtle")
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x, 0)
    x += 50

# Each turtle moves one after another
t1.forward(500)
t2.forward(500)
t3.forward(500)
t4.forward(500)
t5.forward(500)
t6.forward(500)

# Hide the first turtle
t1.hideturtle()

turtle.done()

#Q4
#Each turtle moves at a different speed. Some turtles move faster than others, making the conga line spread out instead of staying together.

#Q5
t1.forward(500)
t1.hideturtle()