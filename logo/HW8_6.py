import numpy as np


def normalize(a):
    return a / max(abs(np.max(a)), abs(np.min(a)))


matrix = np.array([[1, 2, 3], [4, 5, -10]])
matrix = normalize(matrix)
print(matrix)
