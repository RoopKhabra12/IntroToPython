#1 Review
##import turtle
##julia = turtle.Turtle()
##julia.fillcolor("pink") # sets fill colour to pink
##julia.pencolor("black") # sets pen colour to black
##julia.begin_fill() # the shape between here and end_fill
##julia.circle(100) # will be filled in pink
##julia.end_fill() # we've drawn a circle of size 100

##import turtle
##chris = turtle.Turtle()
##chris.write("(0,0)")
##chris.penup()
##chris.goto(-300,0) # our turtle will go to this location
##chris.write("(-300,0)")
##chris.goto(300,0) # goto always needs 2 numbers, X then Y
##chris.write("(300,0)")
##chris.goto(0,-300)
##chris.write("(0,-300)")
##chris.goto(0,300)
##chris.write("(0,300)")
##
###Q1
##chris.penup()
##chris.goto(0,100)
##chris.pendown()
##chris.write("0,100")
##chris.color("yellow")
##chris.stamp()
##
##chris.penup()
##chris.goto(-250,250)
##chris.pendown()
##chris.write("-250,250")
##chris.color("brown")
##chris.stamp()
##
##chris.penup()
##chris.goto(-150,-250)
##chris.pendown()
##chris.write("-150,-250")
##chris.color("teal")
##chris.stamp()
##
##chris.penup()
##chris.goto(0,200)
##chris.pendown()
##chris.write(0,200)
##chris.color("magenta")
##chris.color("black")
##chris.stamp()
###Q2
##chris.goto(0,0)
##chris.circle(50)
##
###Q3
##chris.penup()
##chris.goto(200,200)
##chris.pendown()
##for i in range(4):
##    chris.forward(100)
##    chris.right(90)
##
###Q4
##chris.penup()
##chris.goto(-300,-200)
##chris.pendown()
##for i in range(3):
##    chris.forward(100)
##    chris.right(120)
##
###Q5
##chris.penup()
##chris.goto(0,300)
##chris.pendown()
##chris.fillcolor("green")
##chris.begin_fill()
##chris.circle(40)
##chris.end_fill()
##turtle.done()                
