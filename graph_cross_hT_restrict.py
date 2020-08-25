import matplotlib.pyplot as plt
import numpy as np
from scipy import special

fig = plt.figure()

n = 26 # number of lines

colors = plt.cm.brg(np.linspace(0,1,n)) # blue-red-green colormap

a_range = np.linspace(0,1,n) # different fixed a
h = np.linspace(0,6.3,631)

for i in range(len(a_range)):
    a = a_range[i]
    T = special.owens_t(h,a)

    plt.plot(h,T, color=colors[i])

plt.title("Restricted h*T Cross Sections (a: brg through time)")
plt.xlabel("h")
plt.ylabel("T", rotation=0)
plt.show()
