import numpy as np
from scipy import special, interpolate
import matplotlib.pyplot as plt

n = 63000001 # density of h_range
knots = 50 # number of knots
h_index = 100 # which fixed h

h_range = np.linspace(0.,6.3,n) # different fixed h
h_value = h_range[h_index]

a_train = np.linspace(0.,1.,knots)
T_train = special.owens_t(h_value,a_train)

cs = interpolate.CubicSpline(a_train,T_train)

# Testing spline

max_diff = 0
max_a = 0
a_all = np.linspace(0.,1.,101)

for a_test in a_all:
    ACTUAL = special.owens_t(h_value,a_test)
    SPLINE = cs(a_test)
    DIFF = abs(ACTUAL-SPLINE)
    #print("h = {}".format(h_test))
    #print("ACTUAL: {}".format(ACTUAL))
    #print("SPLINE: {}".format(SPLINE))
    #print("DIFF: {}".format(DIFF))
    max_diff = max(max_diff, DIFF)
    if max_diff==DIFF:
        max_a = a_test

print(max_diff)
print(max_a)