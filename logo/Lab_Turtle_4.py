import turtle   # Упражнение 5
turtle.shape('turtle')
n = int(10)
while n <= 200:
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.left(90)
    turtle.forward(n)
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.pendown()
    n += 20
