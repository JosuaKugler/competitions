from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0.01, 0.99, 99)
theta = np.linspace(0.01 * np.pi, 0.49 * np.pi, 49)
r, theta = np.meshgrid(r, theta)

default = 1.9999000000005003
def S(a, b):
    return a*b/np.sqrt(-a**2 - b**2 + 1) + a*np.sqrt(-a**2 - b**2 + 1)/b + b*np.sqrt(-a**2 - b**2 + 1)/a

X = r * np.sin(theta)
Y = r * np.cos(theta)
Z = S(X, Y)
Z = np.log10(Z)

ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')

plt.show()