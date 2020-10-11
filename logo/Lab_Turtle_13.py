# Упражнение 14
import turtle
turtle.shape('turtle')
n = int(turtle.textinput('Введите количество вершин', 'Введите количество вершин: '))


def twinkle_star(k):
    turtle.left(180 - (180 / k))
    turtle.forward(200)


x = 1
while x <= n:
    twinkle_star(n)
    x += 1
