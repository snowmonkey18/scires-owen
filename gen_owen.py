import numpy as np
from scipy import special
import csv

h_dim = 631
a_dim = 101

h_list = np.linspace(0.,6.3,h_dim).tolist()
a_list = np.linspace(0.,1.,a_dim).tolist()

data_owen = []

for i in range(h_dim):
    h = h_list[i]
    for j in range(a_dim):
        a = a_list[j]
        T = special.owens_t(h,a)
        data_owen.append([h,a,T])

with open("data_owen.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data_owen)