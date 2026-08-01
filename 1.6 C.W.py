###Review
##import turtle
##kayla = turtle.Turtle()
##obie = turtle.Turtle()
##john = turtle.Turtle()
##holly = turtle.Turtle() # we made 4 different turtles!
##kayla.color("red")
##obie.color("green")
##john.color("purple")
##holly.color("orange") # they all change colour one by one
##kayla.speed(1)
##obie.speed(0)
##john.speed(4) # who is the fastest?
##kayla.goto(0,100) # remember week 4 - all about the grid!
##obie.goto(100, 0) # where will they end up?
##john.goto(-100, 0)
##holly.goto(0, -100)
##kayla.hideturtle() # kayla will disappear!

##screen = turtle.Screen() # this is like creating a turtle
### but this time we are creating a Screen
##screen.bgcolor("light blue") # set the colour
##screen.setup(300, 300) # set the size

##import turtle
##screen = turtle.Screen()
##screen.bgcolor("light blue")
##screen.setup(700,400)
##bob = turtle.Turtle()
##bob.color("red")
##bob.circle(50)
##turtle.done()

##import turtle
##sasha = turtle.Turtle() # creating a turtle
##screen = turtle.Screen() # creating a screen
##screen.bgcolor("yellow") # make the screen yellow
##sasha.forward(100) # sasha draws a triangle
##sasha.right(120)
##sasha.forward(100)
##sasha.right(120)
##sasha.forward(100)
##screen.reset() # the triangle is gone!
##sasha.forward(100)
##screen.clear() # everything is gone!

import turtle
screen = turtle.Screen()
screen.bgcolor("light blue")
screen.setup(800,500)
rainbow = turtle.Turtle()
rainbow.speed(2)
rainbow.penup()

# Red
rainbow.goto(0,-350)
rainbow.color("red")
rainbow.begin_fill()
rainbow.pendown()
rainbow.circle(200)
rainbow.end_fill()

# Orange
rainbow.color("orange")
rainbow.begin_fill()
rainbow.pendown()
rainbow.circle(180)
rainbow.end_fill()

# Yellow
rainbow.color("yellow")
rainbow.begin_fill()
rainbow.pendown()
rainbow.circle(160)
rainbow.end_fill()

# Green
rainbow.color("green")
rainbow.begin_fill()
rainbow.pendown()
rainbow.circle(140)
rainbow.end_fill()

# Blue
rainbow.color("blue")
rainbow.begin_fill()
rainbow.pendown()
rainbow.circle(120)
rainbow.end_fill()

# Purple
rainbow.color("purple")
rainbow.begin_fill()
rainbow.pendown()
rainbow.circle(100)
rainbow.end_fill()

rainbow.color("light blue")
rainbow.begin_fill()
rainbow.pendown()
rainbow.circle(80)
rainbow.end_fill()

cloud = turtle.Turtle()
cloud.speed(0)
cloud.color("white")

cloud.penup()
cloud.goto(-220,70)
cloud.pendown()

cloud.begin_fill()
cloud.circle(25)

cloud.penup()
cloud.goto(-190,90)
cloud.pendown()
cloud.circle(30)

cloud.penup()
cloud.goto(-155,70)
cloud.pendown()
cloud.circle(25)
cloud.end_fill()
