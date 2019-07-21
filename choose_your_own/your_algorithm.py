#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

# K nearest neighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from time import time

print("K nearest neighbors =======================")
#print(len(features_test)
clf = KNeighborsClassifier(n_neighbors=13, p=2, metric='euclidean')

t0 = time()
clf = clf.fit(features_train, labels_train)
print("tempo de treinamento:", round(time()-t0, 3), "s")

t0 = time()
pred = clf.predict(features_test)
print("tempo de predição:", round(time()-t0, 3), "s")

acc = accuracy_score(labels_test, pred)
print(acc)

print("AdaBoost =======================")
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier

clf_adaboost = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), n_estimators=50)
#clf_adaboost = AdaBoostClassifier(n_estimators=100)

t0 = time()
clf_adaboost = clf_adaboost.fit(features_train, labels_train)
print("tempo de treinamento:", round(time()-t0, 3), "s")

t0 = time()
pred_adaboost = clf_adaboost.predict(features_test)
print("tempo de predição:", round(time()-t0, 3), "s")

acc = accuracy_score(labels_test, pred_adaboost)
print(acc)

print("RandomForest =======================")
from sklearn.ensemble import RandomForestClassifier
rnd_clf = RandomForestClassifier(n_estimators=100, max_leaf_nodes=4, n_jobs=2, random_state=0)

t0 = time()
rnd_clf = rnd_clf.fit(features_train, labels_train)
print("tempo de treinamento:", round(time()-t0, 3), "s")

t0 = time()
pred_rnd = rnd_clf.predict(features_test)
print("tempo de predição:", round(time()-t0, 3), "s")

#print(rnd_clf.predict_proba(features_test))[0:10]

acc = accuracy_score(labels_test, pred_rnd)
print(acc)

try:
    #prettyPicture(clf, features_test, labels_test)
    prettyPicture(clf_adaboost, features_test, labels_test)
except NameError:
    pass

