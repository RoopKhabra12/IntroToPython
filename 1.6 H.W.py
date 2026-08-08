import turtle

screen = turtle.Screen()
screen.bgcolor("black")

a = turtle.Turtle()
b = turtle.Turtle()
c = turtle.Turtle()
d = turtle.Turtle()

a.shape("turtle")
b.shape("turtle")
c.shape("turtle")
d.shape("turtle")

a.color("blue")
b.color("purple")
c.color("grey")
d.color("red")

a.penup()
b.penup()
c.penup()
d.penup()

a.goto(50, 0)
b.goto(-50, 0)
c.goto(100, 0)
d.goto(-100, 0)

screen.bgcolor("pink")

a.right(90)
b.right(120)
c.right(45)
d.right(150)

a.goto(50, 50)
b.goto(-50, 50)
c.goto(100, -50)
d.goto(-100, -50)

screen.bgcolor("light blue")

a.left(180)
b.left(90)
c.left(120)
d.left(60)

a.goto(0, 100)
b.goto(0, -100)
c.goto(150, 0)
d.goto(-150, 0)

screen.bgcolor("yellow")

a.right(45)
b.right(135)
c.left(90)
d.left(45)

a.goto(80, 80)
b.goto(-80, -80)
c.goto(80, -80)
d.goto(-80, 80)

turtle.done()

#Bonus
roop = turtle.Turtle()
roop.shape("turtle")
roop.color("green")
roop.penup()
screen.onclick(roop.goto)