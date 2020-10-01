import timeit
import numpy as np
from scipy import special
import csv

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
            T = special.owens_t(h,a)
    end = timeit.default_timer()

    this_time = end-start
    min_time = min(min_time, this_time)

print(min_time)


##--------------------------------------------
## Way 2 of timing (idk how to do with quad though)

#n_iter = 100 # number of times iterated for each timer
#n_fmin = 100 # number of tests to find minimum

## Initial method of generating random h and a
#n_rand = 10000 # number of random h and a generated
#h = np.random.uniform(0,6.3,n_rand)
#a = np.random.uniform(0,1,n_rand)

## Get data already generated using above method
#with open('data_owen_speed.csv', 'r') as read_obj:
#    # pass the file object to reader() to get the reader object
#    csv_reader = csv.reader(read_obj)
#    # Pass reader object to list() to get a list of lists
#    row_list = list(csv_reader)

#row_array = np.array(row_list,float)

#h = row_array[0]
#a = row_array[1]

## Timing owen
#min_time = 10**10

#for i in range(n_fmin):
#    this_time = timeit.timeit(lambda: special.owens_t(h,a), number=n_iter)
#    min_time = min(min_time, this_time)

#print(min_time)

##------------------------------------------------
## Way 3 to time
#n_fmin = 20 # number of tests to find minimum

#h_dim = 631
#a_dim = 101

#h_list = np.linspace(0.,6.3,h_dim).tolist()
#a_list = np.linspace(0.,1.,a_dim).tolist()

#min_time = 10**5

#for fmin in range(n_fmin):
#    start = timeit.default_timer()
#    for i in range(h_dim):
#        h = h_list[i]

#        for j in range(a_dim):
#            a = a_list[j]
#            T = special.owens_t(h,a)
#    end = timeit.default_timer()

#    this_time = end - start
#    min_time = min(min_time, this_time)

#print(min_time)

##-----------------------------------------------
## Initial writing of random h and a data

#h_list = h.tolist()
#a_list = a.tolist()
#ha_list = [h_list,a_list]

#with open("data_owen_speed.csv", "w", newline="") as f:
#    writer = csv.writer(f)
#    writer.writerows(ha_list)
