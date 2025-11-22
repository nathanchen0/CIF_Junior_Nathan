import turtle
from random import randint
turtle.bgcolor("black")
turtle.speed(0)
turtle.shape("arrow")

turtle.goto(100, -250)


#Drawing the box
turtle.seth(0)
turtle.goto(75, -250)
turtle.pendown()

turtle.fillcolor("red")
turtle.pencolor("red")

turtle.begin_fill()
for i in range (4):
    turtle.forward(50)
    turtle.right(90)

turtle.end_fill()

#drawing the line
turtle.goto(100, -250)
turtle.seth(90)
turtle.color("white")
turtle.pencolor("white")
for i in range(25):
    turtle.forward(15)
    turtle.left(1)

turtle.done()
