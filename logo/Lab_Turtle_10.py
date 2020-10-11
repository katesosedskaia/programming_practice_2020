# Упражнение 11
import turtle

turtle.shape('turtle')
n = int(30)
turtle.right(90)
while n <= 200:
    turtle.circle(n, 360)
    turtle.circle(-n, 360)
    n += 5
