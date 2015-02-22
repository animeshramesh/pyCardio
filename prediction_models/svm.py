__author__ = 'Animesh'

import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn import svm

input, data, features, results = ([] for i in range(4))
path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'dataset/statlog/data.txt'))
with open(path) as f:
    input = f.readlines()


for line in input:
    each_row = line.split()
    each_row = [float(i) for i in each_row]
    data.append(each_row)
    results.append(each_row.pop())
    features.append(each_row)

results = [int(i) for i in results]

training_features = features[0:230]
training_results = results[0:230]

testing_features = features[230:]
testing_results = results[230:]

clf = svm.SVC(kernel='linear', C = 1.0)
clf.fit(training_features, training_results)

errors = 0
for i in range(len(testing_features)):
    res = clf.predict(testing_features[i])
    if res != testing_results[i]:
        errors += 1

print errors
print len(testing_features)

#test_x1 = [float(i) for i in ['70.0', '1.0', '4.0', '130.0', '322.0', '0.0', '2.0', '109.0', '0.0', '2.4', '2.0', '3.0', '3.0']]
#print (clf.predict(test_x1))
#plt.scatter(x,y)
#plt.show()


