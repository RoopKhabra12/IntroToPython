#Review
import turtle
kayla = turtle.Turtle()
obie = turtle.Turtle()
john = turtle.Turtle()
holly = turtle.Turtle() # we made 4 different turtles!
kayla.color("red")
obie.color("green")
john.color("purple")
holly.color("orange") # they all change colour one by one
kayla.speed(1)
obie.speed(0)
john.speed(4) # who is the fastest?
kayla.goto(0,100) # remember week 4 - all about the grid!
obie.goto(100, 0) # where will they end up?
john.goto(-100, 0)
holly.goto(0, -100)
kayla.hideturtle() # kayla will disappear!

screen = turtle.Screen() # this is like creating a turtle
# but this time we are creating a Screen
screen.bgcolor("light blue") # set the colour
screen.setup(300, 300) # set the size
