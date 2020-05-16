# coding=utf-8
import matplotlib.pyplot as pl
import numpy as np
from pylab import *
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-100, 100, 0.5)
y = np.arange(-100, 100, 0.5)
x, y = meshgrid(x, y)
z = np.sqrt(10000 - np.power(x, 2) - np.power(x, 2))

figure = pl.figure()
ax = Axes3D(figure)
ax.plot_surface(x, y, z)
pl.show()
