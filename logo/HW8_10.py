import numpy as np


def f(b):  # сортирует по строкам
    a_b = b[b[:, 2].argsort()]
    return a_b


matrix = np.array([[3, 2, 4], [6, 1, 3], [4, 4, 8]])
matrix = f(matrix)
print(matrix)
