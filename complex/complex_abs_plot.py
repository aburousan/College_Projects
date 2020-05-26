from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np


def f(x,y):
    z = x+1j*y
    w = abs(1/(z*(z-2)**3))
    w[w>40]=40
    return w 

label = '$\\frac{1}{z(z-2)^2}$'

fig = plt.figure(figsize=(9,5))
ax = Axes3D(fig)
ax.set_zlim(-2,30)
X = np.linspace(-0.5,3, 300)
Y = np.linspace(-1, 1, 300)
X, Y = np.meshgrid(X, Y)

ax.text(1,1,15,label,fontsize=20)
sur = ax.plot_surface(X, Y, f(X,Y), cmap=cm.jet)
fig.colorbar(sur,shrink=0.6)

plt.xlabel("Real")
plt.ylabel("Imaginary")
plt.title("Abs of complex functions")
plt.show()
