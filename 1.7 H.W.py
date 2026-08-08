import turtle
from random import randint

# create a screen object called 'screen'
screen = turtle.Screen()

# set the background colour to black
screen.bgcolor("black")

# create a turtle named 'me' this will be the turtle you control
me = turtle.Turtle()

# set the turtle's colour to your favourite colour
me.color("red")

# create a new turtle named 'dot', they will draw the stars
dot = turtle.Turtle()

# set dot's speed to 0
dot.speed(0)

# dot needs to lift their pen
dot.penup()

# dot needs to be invisible
dot.hideturtle()

# set dot's colour to white
dot.color("white")

screen.onclick(me.goto)

for i in range(20):
    dot.goto(randint(-200,200), randint(-200,200))
    dot.begin_fill()
    dot.circle(randint(3,10))
    dot.end_fill()