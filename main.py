from matplotlib import cm # Para manejar colores
import numpy as np
import matplotlib.pyplot as plt

# graph on 3D
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})


res = 100

X = np.linspace(-4, 4, res)
Y = np.linspace(-4, 4, res)

X, Y = np.meshgrid(X, Y)

Z = np.sin(X) + 2*np.sin(Y)

surf = ax.plot_surface(X, Y, Z, cmap=cm.cool, linewidth=0, antialiased=False)

fig.colorbar(surf)


# countour lines
fig2,ax2 = plt.subplots()
level_map = np.linspace(np.min(Z), np.max(Z),res)
cp = ax2.contour(X, Y, Z, levels=level_map,cmap=cm.cool)
fig2.colorbar(cp)
ax2.set_title('Level curves')


fig3,ax3 = plt.subplots()
cp = ax3.contourf(X, Y, Z, levels=level_map,cmap=cm.cool)
fig3.colorbar(cp)
ax3.set_title('Level colors')
plt.show()



