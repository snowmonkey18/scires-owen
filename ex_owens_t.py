from scipy.special import owens_t
from scipy.stats import norm
from math import pi, atan, inf

# Parameters of function
h = 0.78
a = 3.5

# Formula 2.3

def eq_2_3(h,a):
    '''Use to obtain values for 1<a<inf'''
    term1 = 1/2*norm.cdf(h)
    term2 = 1/2*norm.cdf(a*h)
    term3 = -norm.cdf(h)*norm.cdf(a*h)
    term4 = -owens_t(a*h,1/a)
    return term1 + term2 + term3 + term4

if a>1:
    print('T('+str(h)+','+str(a)+') = '+str(eq_2_3(h,a))+' by formula 2.3')

# Formula (2.4) and (2.5)
h_a = owens_t(h,a)
h_na = owens_t(h,-a)
nh_a = owens_t(-h,a)

print('T('+str(h)+','+str(a)+') = '+str(h_a))
print('T('+str(h)+','+str(-a)+') = '+str(h_na))
print('T('+str(-h)+','+str(a)+') = '+str(nh_a))

print(owens_t(h,0))
print(owens_t(0,a))
print(1/2/pi*atan(a))
print(owens_t(h,1))
print(1/2*norm.cdf(h)*(1-norm.cdf(h)))
print(owens_t(h,10**16))
print(owens_t(h,inf))
print(1/2*(1-norm.cdf(h)))

h = 1
a = -3
owens_t(h,2*10**a) - owens_t(h,1*10**a)