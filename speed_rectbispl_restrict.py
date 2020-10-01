import pickle
import csv
import numpy as np
import timeit

with open('rectbispl.pkl', 'rb') as f:
    rectbispl = pickle.load(f)

# Get data already generated using method 2
with open('data_owen_test.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    test_list = list(csv_reader)

test_array = np.array(test_list,float)
ha_array = test_array[:,0:2]

# Timing owen
n_fmin = 10 # number of tests to find minimum
min_time = 10**5

for fmin in range(n_fmin):
    start = timeit.default_timer()
    for h,a in ha_array:
        T = rectbispl(h,a)
    end = timeit.default_timer()

    this_time = end-start
    min_time = min(min_time, this_time)

print(min_time)
