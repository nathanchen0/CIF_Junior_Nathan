import turtle

#drawing a circle flower
turtle.bgcolor("black")
turtle.speed(0)
turtle.shape("turtle")
turtle.color("red")
length = 10
for i in range(20):
    #turtle.goto(0,0)
    for j in range(18):
        turtle.forward(length)
        turtle.right(18)
    length += 5

turtle.done()
