# coding=utf-8
import matplotlib.pyplot as plot
import numpy as np
import matplotlib
import random

font = {
    "family": "SimHei",
    "size": 26
}
plot.rc("font", **font)
plot.rc("axes", unicode_minus=False)

def y_5():
    x = np.arange(5)
    y = np.power(x, 5)
    plot.xlabel("x")
    plot.ylabel("y")
    plot.title("y = x^5")
    plot.plot(x, y)
    plot.show()


def y_2():
    x = np.arange(0, 20, 1)
    y = np.power(x, 2)
    plot.plot(x, y, "o")
    plot.show()


def poit_plot():
    i = 0
    x = []
    for i in range(10):
        x.append(random.randint(0, 10))
        i += 1
    plot.plot(x, np.sin(x), 'o')
    plot.show()


def y_3():
    x = np.arange(0, 20, 1)
    y = np.power(x, 2)
    plot.plot(x, y, "--g", label="嗷嗷嗷")
    plot.legend()
    plot.show()


if __name__ == "__main__":
    y_3()
