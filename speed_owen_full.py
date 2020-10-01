import timeit
import numpy as np
from scipy import special

n_fmin = 20 # number of tests to find minimum

h_dim = 631
a_dim = 101

h_list = np.linspace(-6.3,6.3,h_dim).tolist()
a_list = np.linspace(-20,20,a_dim).tolist()

min_time = 10**5

for fmin in range(n_fmin):
    start = timeit.default_timer()
    for i in range(h_dim):
        h = h_list[i]

        for j in range(a_dim):
            a = a_list[j]
            T = special.owens_t(h,a)
    end = timeit.default_timer()

    this_time = end - start
    min_time = min(min_time, this_time)

print(min_time)