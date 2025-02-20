#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
from sklearn.svm import SVC
clf = SVC(C=10000.0, kernel="rbf") #SVC(kernel="linear")

#features_train = features_train[0:int(len(features_train)/100)] 
#labels_train = labels_train[0:int(len(labels_train)/100)] 
t0 = time()
clf.fit(features_train, labels_train)  
print("tempo de treinamento:", round(time()-t0, 3), "s")

#### store your predictions in a list named pred
t0 = time()
pred = clf.predict(features_test)
print("tempo de predicao:", round(time()-t0, 3), "s")

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print(acc)

print(pred[10])

print(pred[26])

print(pred[50])

print(len([i for i in pred if i == 1]))
#########################################################


