import turtle

turtle.bgcolor("black")
turtle.color("black")
turtle.shape("circle")
turtle.shapesize(0.5)
turtle.speed(0)
#ground
turtle.penup()
turtle.goto(-400, -250)
turtle.pendown()
turtle.pencolor("green")
turtle.fillcolor("green")
turtle.begin_fill()
turtle.forward(800)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()

turtle.penup()
turtle.goto(150, -250)
turtle.pendown()

turtle.begin_fill()
turtle.pencolor("red")
turtle.fillcolor("red")
#draw the box of the fireworks
for i in range(4):
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.goto(125, -200)
turtle.seth(90)
turtle.pendown()
#launch firework
turtle.color("white", "white")
#turn firework
turtle.speed(3)
for i in range(50):
    turtle.forward(9)
    turtle.left(1)

turtle.color("yellow")
size = 1
for i in range(5):
    size += 0.2
    turtle.shapesize(size)

trtls = []*36

color = ["yellow", "red", "orange", "yellow", "red", "orange", "yellow", "red", "orange", "yellow", "red", "orange", "yellow", "red", "orange", "yellow", "red", "orange"]

print("Here!")
turtle.delay(0)
for i in range(18):
    trtls.append(turtle.clone())
    trtls[i].speed(0)
    trtls[i].right(20*i)
    #trtls[i].color("black")
    trtls[i].shapesize(0.1)
    trtls[i].pencolor(color[i % len(color)])
    print(i)

for j in range(50):
    for i in range(18):
        trtls[i].forward(3)

print("done")

turtle.done()
