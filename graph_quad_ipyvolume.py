import ipyvolume as ipv
import numpy as np

data_quad = np.genfromtxt('data_quad.csv', delimiter=',')
x, y, z = data_quad.T

ipv.quickscatter(x, y, z, size=1, marker="sphere")