import matplotlib.pyplot as plt
import numpy as np
from scipy import special

fig = plt.figure()

n = 64 # number of lines

colors = plt.cm.brg(np.linspace(0,1,n)) # blue-red-green colormap

h_range = np.linspace(0,6.3,n) # different fixed h
a = np.linspace(0,1,101)

for i in range(len(h_range)):
    h = h_range[i]
    T = special.owens_t(h,a)

    plt.plot(a,T, color=colors[i])

plt.title("Restricted a*T Cross Sections (h: brg through time)")
plt.xlabel("a")
plt.ylabel("T", rotation=0)
plt.show()

