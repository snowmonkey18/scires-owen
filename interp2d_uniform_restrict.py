import csv
import numpy as np
from scipy import special, interpolate
import pickle

## Train on uniform data

#with open('data_owen_all.csv', 'r') as read_obj:
#    # pass the file object to reader() to get the reader object
#    csv_reader = csv.reader(read_obj)
#    # Pass reader object to list() to get a list of lists
#    train_list = list(csv_reader)

#train_array = np.array(train_list,float).T
#h_train,a_train,T_train = train_array

h_dim = 631
a_dim = 101

h_train = np.linspace(0.,6.3,h_dim)
a_train = np.linspace(0.,1.,a_dim)
hh,aa = np.meshgrid(h_train,a_train)
T_train = special.owens_t(hh,aa)

interp1 = interpolate.interp2d(h_train,a_train,T_train, 
                                kind='linear', 
                                fill_value=-100)

interp3 = interpolate.interp2d(h_train,a_train,T_train, 
                                kind='cubic', 
                                fill_value=-100)

interp5 = interpolate.interp2d(h_train,a_train,T_train, 
                                kind='quintic', 
                                fill_value=-100)

# Accuracy test on random data

max_diff1,max_diff3,max_diff5 = 0,0,0
max_ha1,max_ha3,max_ha5 = (0,0), (0,0), (0,0)

with open('data_owen_test.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    test_list = list(csv_reader)

test_array = np.array(test_list,float)
ha_array = test_array[:,0:2]

for h_test,a_test in ha_array:
    ACTUAL = special.owens_t(h_test,a_test)
    INTERP1 = interp1(h_test,a_test)
    INTERP3 = interp3(h_test,a_test)
    INTERP5 = interp5(h_test,a_test)
    DIFF1 = abs(ACTUAL-INTERP1)
    DIFF3 = abs(ACTUAL-INTERP3)
    DIFF5 = abs(ACTUAL-INTERP5)
    #print("h = {}".format(h_test))
    #print("ACTUAL: {}".format(ACTUAL))
    #print("SPLINE: {}".format(SPLINE))
    #print("DIFF: {}".format(DIFF))
    max_diff1 = max(max_diff1, DIFF1)
    max_diff3 = max(max_diff3, DIFF3)
    max_diff5 = max(max_diff5, DIFF5)
    if max_diff1==DIFF1:
        max_ha1 = h_test,a_test
    if max_diff3==DIFF3:
        max_ha3 = h_test,a_test
    if max_diff5==DIFF5:
        max_ha5 = h_test,a_test

print(f"Linear\n{max_diff1}\n{max_ha1}")
print(f"Cubic\n{max_diff3}\n{max_ha3}")
print(f"Quintic\n{max_diff5}\n{max_ha5}")
    

# Write to pickles
with open('interp1.pkl', 'wb') as f:
    pickle.dump(interp1, f)
with open('interp3.pkl', 'wb') as f:
    pickle.dump(interp3, f)
with open('interp5.pkl', 'wb') as f:
    pickle.dump(interp5, f)

# Read from pickles
#with open('interp1.pkl', 'rb') as f:
#    interp1_loaded = pickle.load(f)

