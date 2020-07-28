import numpy as np
import math
import scipy as sp

h_dim = 1001
a_dim = 1001

h_list = np.linspace(0,10,h_dim).tolist()
a_list = np.linspace(0,1,a_dim).tolist()

quad_results = np.ones((h_dim,a_dim))

for i in range(h_dim):
    h = h_list[i]
    f = lambda x: 1/2/math.pi*(np.exp(-h**2*(1+x**2)/2))/(1+x**2)
    for j in range(a_dim):
        a = a_list[j]
        quad_results[i][j] = sp.integrate.quad(f,0,a)[0]
