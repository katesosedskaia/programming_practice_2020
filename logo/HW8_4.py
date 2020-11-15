import numpy as np

m = np.random.randint(10, 101)  # задает случайную размерность матрицы
print(m)

matrix = np.random.sample((m, m))  # создает случайную матрицу
print(matrix)

max_value = np.max(matrix)  # находит максимум
print(max_value)

matrix = matrix / max_value  # делит каждый элемент матрицы на максимум
print(matrix)

s = matrix.sum()  # находит сумму элементов
print(s)

matrix = matrix - np.mean(matrix, axis=1)  # отнимает от каждой строки матрицы среднее по строке.
print(matrix)

matrix[matrix == max_value] = -1   # заменяет максимальное значение на -1
print(matrix)
