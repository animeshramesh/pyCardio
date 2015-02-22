__author__ = 'Animesh'

import os

data = []
path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'dataset/statlog/data.txt'))
with open(path) as f:
    data = f.readlines()

num_data = []
for line in data:
    each_row = line.split()
    num_data.append(each_row)

