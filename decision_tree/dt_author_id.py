#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)

print("tamanho dados:", len(features_train[0]))

t0 = time()
clf = clf.fit(features_train, labels_train)
print("tempo de treinamento:", round(time()-t0, 3), "s")

t0 = time()
pred = clf.predict(features_test)
print("tempo de predicao:", round(time()-t0, 3), "s")

from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, pred)

print(acc)

#########################################################


