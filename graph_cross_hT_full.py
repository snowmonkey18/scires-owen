import matplotlib.pyplot as plt
import numpy as np
from scipy import special

fig = plt.figure()

n = 201 # number of lines

colors = plt.cm.brg(np.linspace(0,1,n)) # blue-red-green colormap

a_range = np.linspace(-20,20,n) # different fixed a
h = np.linspace(-6.3,6.3,127)

for i in range(len(a_range)):
    a = a_range[i]
    T = special.owens_t(h,a)

    plt.plot(h,T, color=colors[i])

plt.title("Full h*T Cross Sections (a: brg through time)")
plt.xlabel("h")
plt.ylabel("T", rotation=0)
plt.show()
