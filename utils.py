import numpy as np
from numpy.random import normal

def func1(a):
    return a + 3

def func2(a):
    b = func1(a)
    return b ** 2

def func3(a):
    b = np.exp(a)
    print(b)
    return b

def func4(a, b):
    counter = 0
    for i in range(b):
        counter += a
    return counter