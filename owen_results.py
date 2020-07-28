import numpy as np
import math
import scipy as sp

h_dim = 1001
a_dim = 1001

h_list = np.linspace(0,10,h_dim).tolist()
a_list = np.linspace(0,1,a_dim).tolist()

owen_results = np.ones((h_dim,a_dim))

for i in range(h_dim):
    h = h_list[i]
    for j in range(a_dim):
        a = a_list[j]
        owen_results[i][j] = sp.special.owens_t(h,a)
