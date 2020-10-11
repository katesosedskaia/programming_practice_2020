# Упражнение 7
import turtle
turtle.shape('turtle')
k = 1  # смещение точки M по лучу r при повороте на угол, равный одному радиану.
alfa_radian = 0.1  # угол в радианах
alfa_degrees = alfa_radian * (180 / 3.14)  # переведем радианы в градусы
for i in range(0, 1000):
    P = k * alfa_radian  # уравнение Архимедовой спирали
    turtle.forward(P)
    turtle.left(alfa_degrees)
    alfa_radian += 0.1
    P += P
