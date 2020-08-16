import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

x1 = np.linspace(0,6,100).reshape(-1,1)
x2 = np.logspace(0,10,100).reshape(-1,1)

y = 5*x1-2*x2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
_ = ax.scatter(xs=x1, ys=x2, zs=y)
_ = ax.plot_wireframe(X=x1, Y=x2, Z=y, rstride=5, cstride=5)

#for angle in range(0, 360):
 #   _ = ax.view_init(30, angle)
  #  _ = plt.draw()
   # _ = plt.pause(.001)