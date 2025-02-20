#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
words_handler = open(words_file, 'rb')
word_data = pickle.load(words_handler)
authors_handler = open(authors_file, 'rb')
authors = pickle.load(authors_handler)


### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]


### your code goes here
print(len(features_train))

from sklearn import tree
from time import time
clf = tree.DecisionTreeClassifier()

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

importances  = clf.feature_importances_
#print(importances)
very_important = {index:item for index, item in enumerate(importances) if item >= 0.2}
print(very_important)
print(vectorizer.get_feature_names()[list(very_important)[0]])
# https://stackoverflow.com/questions/40370583/how-do-i-do-prediction-after-fitting-tfidfvectorizer-and-kmeans-in-scikit-learn



