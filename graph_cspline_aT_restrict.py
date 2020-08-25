import numpy as np
from scipy import special, interpolate
import matplotlib.pyplot as plt

n = 631 # density of h_range
knots = 3 # number of knots
h_index = 50 # which fixed h

h_range = np.linspace(0.,6.3,n) # different fixed h

h_train = h_range[h_index]
a_train = np.linspace(0,1,knots)
T_train = special.owens_t(h_train,a_train)

h_all = h_range[h_index]
a_all = np.linspace(0.,1.,1001)
T_all = special.owens_t(h_all,a_all)

cs = interpolate.CubicSpline(a_train,T_train)

a_test = np.linspace(0.,1.,1001)
plt.subplots(figsize=(6.5, 4))
plt.plot(a_all, T_all, '.', label = 'real', color='lime')
plt.plot(a_train, T_train, 'o', label='data', color='blue')
plt.plot(a_test, cs(a_test), label="spline", color='red')
plt.plot(a_test, cs(a_test,1), label="spline'", color='black')
plt.plot(a_test, cs(a_test,2), label="spline''", color='gray')
plt.plot(a_test, cs(a_test,3), label="spline'''", color='silver')

#testing spline
#spline_num = 1

#rngA = cs.x[spline_num]
#rngB = cs.x[spline_num + 1]
#coef = cs.c[:,spline_num]

#poly = np.poly1d(coef)
#test = np.arange(rngA, rngB, 0.01)
#plt.plot(test,poly(test-rngA))

plt.legend(loc='lower right', ncol=2)

plt.title("Restricted a*T Cross Section (h=0.5)")
plt.xlabel("a")
plt.ylabel("T", rotation=0)

plt.show()