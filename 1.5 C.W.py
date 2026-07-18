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
