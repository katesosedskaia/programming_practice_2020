import turtle  # Упражнение 9

turtle.shape('turtle')
outset_y = -8


def polygon(n, length):
    angles = (n - 2) * 180  # сумма углов в многоугольнике
    angle = angles / n  # градусная мера углов
    for j in range(n):
        turtle.forward(length)
        turtle.left(180 - angle)


for i in range(3, 13):
    polygon(i, 50)
    turtle.penup()
    turtle.goto(turtle.xcor(), turtle.ycor() + outset_y)
    turtle.pendown()
