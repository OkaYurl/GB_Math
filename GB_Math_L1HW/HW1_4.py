"""
Задание (в программе):
Постройте на одном графике две кривые y(x) для функции двух переменных
y(k,x)=cos(k∙x), взяв для одной кривой значение k=1, а для другой – любое другое k, не
равное 1
"""


import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 5, 0.1)
k1 = 1
y1 = np.cos(k1 * x)
k2 = 2
y2 = np.cos(k2 * x)

fig, axs = plt.subplots(1, 1)
line1, = axs.plot(x, y1)
line2, = axs.plot(x, y2)
fig.legend((line1, line2), ('k=1', 'k=2'), 'upper right')

axs.set(xlabel='X', ylabel='Y', title='График функции y = cos(k*x)')
axs.grid()

fig.savefig("test.png")
plt.show()
