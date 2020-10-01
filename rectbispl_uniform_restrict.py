import csv
import numpy as np
from scipy import special, interpolate
import pickle

# Train on uniform data
h_dim = 3
a_dim = 3

h_train = np.linspace(0.,6.3,h_dim)
a_train = np.linspace(0.,1.,a_dim)
hh,aa = np.meshgrid(h_train,a_train,indexing='ij')
T_train = special.owens_t(hh,aa)

kx_ = 1
ky_ = 1

rectbispl = interpolate.RectBivariateSpline(
                            h_train,a_train,T_train, 
                            kx=kx_, ky=ky_)

# Accuracy test on random data
max_diff = 0
max_ha = (0,0)

with open('data_owen_test.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    test_list = list(csv_reader)

test_array = np.array(test_list,float)
ha_array = test_array[:,0:2]

for h_test,a_test in ha_array:
    ACTUAL = special.owens_t(h_test,a_test)
    SPLINE = rectbispl(h_test,a_test)
    DIFF = (abs(ACTUAL-SPLINE))/(ACTUAL)

    max_diff = max(max_diff, DIFF)
    if max_diff==DIFF:
        max_ha = h_test,a_test

print(f"({h_dim},{a_dim},{kx_},{ky_})\n{max_diff}\n{max_ha}")

# Write to pickle
with open('rectbispl.pkl', 'wb') as f:
    pickle.dump(rectbispl, f)

# Read from pickles
#with open('rectbispl.pkl', 'rb') as f:
#    rectbispl = pickle.load(f)

