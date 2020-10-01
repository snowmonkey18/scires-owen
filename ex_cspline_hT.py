import numpy as np
from scipy import special, interpolate
import matplotlib.pyplot as plt

n = 101 # density of a_range
knots = 310 # number of knots 412
a_index = 100 # which fixed a

a_range = np.linspace(0.,1.,n) # different fixed a
a_value = a_range[a_index]
a_value = 1 #***********FOR TESTING************

h_train = np.linspace(-.015,5.920,knots)
T_train = special.owens_t(h_train,a_value)

cs = interpolate.CubicSpline(h_train,T_train)

# Testing spline

max_diff = 0
max_h = 0
h_all = np.linspace(0.,6.3,6301)

for h_test in h_all:
    ACTUAL = special.owens_t(h_test,a_value)
    SPLINE = cs(h_test)
    DIFF = abs(ACTUAL-SPLINE)
    #print("h = {}".format(h_test))
    #print("ACTUAL: {}".format(ACTUAL))
    #print("SPLINE: {}".format(SPLINE))
    #print("DIFF: {}".format(DIFF))
    max_diff = max(max_diff, DIFF)
    if max_diff==DIFF:
        max_h = h_test

print(max_diff)
print(max_h)
