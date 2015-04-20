__author__ = 'Animesh'
import sys
import numpy as np
from copy import copy, deepcopy

class Normalizer:

    def __init__(self, features):
        self.max_val = [0] * 13
        self.min_val = [1000] * 13
        self.mean = [1] * 13
        self.std_dev = [1] * 13 #standard deviation
        self.real_fatures = [0, 3, 4, 7, 9, 11]
        self.find_max(features)
        self.find_min(features)
        # scaled_features = scale_continuous_features(features)

    def find_max(self, features):
        for each_row in features:
            for i, each_val in enumerate(each_row):
                if self.max_val[i] < each_val:
                    self.max_val[i] = each_val

    def find_min(self, features):
        for each_row in features:
            for i, each_val in enumerate(each_row):
                if self.min_val[i] > each_val:
                    self.min_val[i] = each_val

    def scale_continuous_features(self, features):
        # Real: 1,4,5,8,10,12
        real_fatures = [0, 3, 4, 7, 9, 11]
        scaled_features = []
        for each_row in features:
            new_row = []
            for i, each_val in enumerate(each_row):
                if i in real_fatures:
                    new_row.append((2*each_val - self.max_val[i] - self.min_val[i])/(self.max_val[i] - self.min_val[i]))
                    # sys.stdout.write('%20f' %each_val)
                    # sys.stdout.write(" --> ")
                    # sys.stdout.write('%20f' %new_row[i])
                    sys.stdout.write("\n")
                else:
                    new_row.append(each_val)
                    # new_row.append((2*each_val - self.max_val[i] - self.min_val[i])/(self.max_val[i] - self.min_val[i]))
            scaled_features.append(new_row)
        return scaled_features

    def get_mean(self, features):
        features = np.array(features)
        mean = features.mean(axis=0) #Take the mean over a column
        return mean

    def get_std_dev(self, features):
        std_dev = [1] * 13
        features = np.array(features)
        for i in range(0, 12):
            std_dev[i] = np.std(zip(*features)[i])
        return std_dev

    def standardize_features(self, features):
        mean = self.get_mean(features)  #mean of each column
        #print mean
        std_dev = self.get_std_dev(features) #Standard dev of each column
        #print std_dev

        std_features = [] #Standardized features
        for each_row in features:
            new_row = []
            for i in range(0, 12):
                if i in self.real_fatures:
                    new_row.append((each_row[i] - mean[i]) / std_dev[i])
                else:
                    new_row.append(each_row[i])
                    # new_row.append((each_row[i] - mean[i]) / std_dev[i])
            std_features.append(new_row)
        return std_features

    def binarize_features(self, features):
        #For all categorical features, represent them as multiple boolean features.
        new_features = deepcopy(features)
        for i in range(0, len(features)-1):
            if features[i][1] == 0.0:   #Sex
                new_features[i][1] = -1.0
            if features[i][5] == 0.0:   #Sugar level > 120
                new_features[i][5] = -1.0
            if features[i][8] == 0.0:   #Exercise induced chest pain
                new_features[i][8] = -1.0
        return new_features





