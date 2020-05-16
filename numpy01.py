# coding=utf-8
import numpy as np

def numtest():
    a = np.array([1, 2, 3, ], dtype=float, ndmin=3)
    print(a)
    print(type(a))
    b = range(10)
    print(type(b))

    c = np.random.random(size=5)
    print(type(c))
    print(c)

def test02():
    a = np.arange(1, 21)
    print(a)

    b = a.reshape((4, 5))
    print(b)
    d = b.flatten()
    print(d)
    c = np.reshape(b, b.size)
    print(c)
def test03():
    a = np.arange(0, 20, 2).reshape(10, 1)
    b = np.arange(1, 21, 2).reshape(10, 1)
    c = np.hstack((a, b))
    print(c)

if __name__ == "__main__":
    test03()