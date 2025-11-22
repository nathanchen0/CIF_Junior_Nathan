import turtle

turtle.shape("turtle")
turtle.color("red")
turtle.speed(1)

sides = int(input("Enter the number of sides for the polygon: "))
length = int(input("Enter the length of each side: "))
angle = (sides-2)*180/sides

for i in range(sides):
    turtle.forward(length)
    turtle.left(180 - angle)

turtle.done()
