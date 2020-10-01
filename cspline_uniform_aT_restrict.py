import numpy as np
from scipy import special, interpolate
import matplotlib.pyplot as plt
# add 2 zero to n if needed (don't add 3)
n = 6300001 # density of a_range
knots = 10 # number of knots

a_range = np.linspace(0.,1.,n) # different fixed a
h_train = np.linspace(0.,6.3,knots)

coef_list = []

for a_value in a_range: # which fixed a
    T_train = special.owens_t(h_train,a_value)
    cs = interpolate.CubicSpline(h_train,T_train)
    coef_list.append(cs.c)

