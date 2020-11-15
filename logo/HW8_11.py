import numpy as np


def chess(shape_):
    a = np.zeros((shape_, shape_))
    a[1::2, ::2] = 1
    a[::2, 1::2] = 1
    print(a)


chess(shape_=4)
