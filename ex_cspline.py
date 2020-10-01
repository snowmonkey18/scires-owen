import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8]
y = [10,9,1,5,4,8,0,3]
cs = interpolate.CubicSpline(x,y)

x1 = [3,4,5,6,7]
y1 = [1,5,4,8,0]
cs1 = interpolate.CubicSpline(x1,y1)

test = np.linspace(1,8,1000)

plt.subplots(figsize=(6.5, 4))
plt.plot(x,y,'o', color='black')
plt.plot(test, cs(test), color='black')
plt.plot(test, cs1(test), color='red')
plt.show()