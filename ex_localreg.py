# https://pypi.org/project/localreg/

import numpy as np
import matplotlib.pyplot as plt
from localreg import *

np.random.seed(1234)
x = np.linspace(1.5, 5, 2000)
yf = np.sin(x*x)
y = yf + 0.5*np.random.randn(*x.shape)

y0 = localreg(x, y, degree=2, kernel=gaussian, width=0.1)
y1 = localreg(x, y, degree=2, kernel=sigmoid, width=0.05)
y2 = localreg(x, y, degree=2, kernel=rectangular, width=0.1)

plt.plot(x, y, '+', markersize=0.6, color='gray')
plt.plot(x, yf, label='Ground truth ($\sin(x^2)$)')
plt.plot(x, y0, label='y0')
plt.plot(x, y1, label='y1')
plt.plot(x, y2, label='y2')
plt.legend()
plt.show()