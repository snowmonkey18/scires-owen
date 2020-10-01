import numpy as np
from scipy import special
import csv

n_rand = 100000 # number of random h and a generated
h_array = np.random.uniform(0,6.3,n_rand)
a_array = np.random.uniform(0,1,n_rand)
ha_array = np.vstack([h_array,a_array]).T

test_owen = []

for h,a in ha_array:
        T = special.owens_t(h,a)
        test_owen.append([h,a,T])

with open("data_owen_test.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(test_owen)