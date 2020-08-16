import numpy as np
import math
from scipy import integrate
import csv

h_dim = 631
a_dim = 101

h_list = np.linspace(0,6.3,h_dim).tolist()
a_list = np.linspace(0,1,a_dim).tolist()

data_quad = []

for i in range(h_dim):
    h = h_list[i]
    f = lambda x: 1/2/math.pi*(np.exp(-h**2*(1+x**2)/2))/(1+x**2)
    for j in range(a_dim):
        a = a_list[j]
        T = integrate.quad(f,0,a)[0]
        data_quad.append([h,a,T])

with open("data_quad.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data_quad)