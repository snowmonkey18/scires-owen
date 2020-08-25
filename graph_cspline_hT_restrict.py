import numpy as np
from scipy import special, interpolate
import matplotlib.pyplot as plt

n = 101 # density of a_range
knots = 10 # number of knots
a_index = 100 # which fixed a

a_range = np.linspace(0.,1.,n) # different fixed a

h_train = np.linspace(0.,6.3,knots)
a_train = a_range[a_index]
T_train = special.owens_t(h_train,a_train)

h_all = np.linspace(0.,6.3,6301)
a_all = a_range[a_index]
T_all = special.owens_t(h_all,a_all)

cs = interpolate.CubicSpline(h_train,T_train)

h_test = np.linspace(0.,6.3,6301)
plt.subplots(figsize=(6.5, 4))
plt.plot(h_all, T_all, '.', label = 'real', color='lime')
plt.plot(h_train, T_train, 'o', label='data', color='blue')
plt.plot(h_test, cs(h_test), label="spline", color='red')
plt.plot(h_test, cs(h_test,1), label="spline'", color='black')
plt.plot(h_test, cs(h_test,2), label="spline''", color='gray')
plt.plot(h_test, cs(h_test,3), label="spline'''", color='silver')

# testing spline
#spline_num = 1

#rngA = cs.x[spline_num]
#rngB = cs.x[spline_num + 1]
#coef = cs.c[:,spline_num]

#poly = np.poly1d(coef)
#test = np.arange(rngA, rngB, 0.01)
#plt.plot(test,poly(test-rngA))

plt.legend(loc='upper right', ncol=2)

plt.title("Restricted h*T Cross Section (a=1)")
plt.xlabel("h")
plt.ylabel("T", rotation=0)

plt.show()