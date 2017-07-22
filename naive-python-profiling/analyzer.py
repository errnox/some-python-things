#!/usr/bin/env python

import glob

import matplotlib.pyplot as plt
import numpy as np


data_dir = 'data'
data_sets = []


# Fetch the data

for data_file in glob.glob(data_dir + '/*'):
    with open(data_file, 'r') as file:
        data_sets.append([line for line in file])


# Plot

fig = plt.figure()
ax = fig.add_subplot(111)

for data_set in data_sets:
    ax.plot(data_set)

plt.show()
