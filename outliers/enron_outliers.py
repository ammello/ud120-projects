#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_handler = open("../final_project/final_project_dataset_unix.pkl", "rb")
data_dict = pickle.load(data_handler)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

data = sorted(data, key=lambda x:x[1], reverse=True)   
maior_bonus = data[0][1]
print(maior_bonus)

data = data[1:]

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()


