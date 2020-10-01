import pickle
import csv
import numpy as np
import cProfile
from scipy.special import owens_t

with open('rectbispl.pkl', 'rb') as f:
    rectbispl = pickle.load(f)

# Get data already generated using method 2
with open('data_owen_test.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    test_list = list(csv_reader)

test_array = np.array(test_list,float)
ha_array = test_array[:,0:2]

# profile

pr = cProfile.Profile()
pr.enable()

for i in range(1):
    for h,a in ha_array:
        T = owens_t(h,a)

pr.disable()

pr.print_stats(sort='time')
