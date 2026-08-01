import turtle
a = turtle.Turtle()
w = turtle.Turtle()

# give colors
a.color = ("green")
w.color = ("purple")

# speed
a.speed(0)
w.speed(0) 

# move position 
artist.penup()
artist.goto(0, 100)
artist.pendown()

writer.penup()
writer.goto(-70, -170)

# Draw Circle 1
artist.circle(50)
writer.write("1 done, 4 to go!", font=("Arial", 12, "normal"))

# Draw Circle 2
artist.left(72)
artist.circle(50)
writer.goto(-70, -190)
writer.write("2 done, 3 to go!", font=("Arial", 12, "normal"))

# Draw Circle 3
artist.left(72)
artist.circle(50)
writer.goto(-70, -210)
writer.write("3 done, 2 to go!", font=("Arial", 12, "normal"))

# Draw Circle 4
artist.left(72)
artist.circle(50)
writer.goto(-70, -230)
writer.write("4 done, 1 to go!", font=("Arial", 12, "normal"))

# Draw Circle 5
artist.left(72)
artist.circle(50)
writer.goto(-70, -250)
writer.write("5 done, 0 to go!", font=("Arial", 12, "normal"))

# Congratulations message
writer.goto(-80, -290)
writer.write("Great job, Artist!", font=("Arial", 16, "bold"))

turtle.done()