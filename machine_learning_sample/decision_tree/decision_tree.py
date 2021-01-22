#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/17 17:21
# @Author : MarxZhao
# @File : decision_tree.py
# @Software: PyCharm

from sklearn import datasets
import sklearn.model_selection as ms
from sklearn import tree

data = datasets.load_breast_cancer()

print(data.data.shape)
print(data.feature_names)
print(data.target_names)

# data_pre = data.feature_names
# target = data.target_names

X_train, X_test, y_train, y_test = ms.train_test_split(data.data, data.target, test_size=0.2, random_state=42)

dtc = tree.DecisionTreeClassifier()
dtc.fit(X_train, y_train)
tree.DecisionTreeClassifier(class_weight=None, criterion='gini',
                            max_depth=None, max_features=None,
                            max_leaf_nodes=None,
                            min_impurity_split=1e-07,
                            min_samples_leaf=1,
                            min_samples_split=2, random_state=None,
                            splitter='best')

score = dtc.score(X_train, y_train)

test_score = dtc.score(X_test, y_test)

print(score, test_score)
with open("tree.dot", 'w') as f:
    f = tree.export_graphviz(dtc, out_file=f, feature_names=data.feature_names,
                             class_names=data.target_names)


#研究决策树深度对性能影响

train_score = []
test_score = []
for i in range(1, 10, 2):
    dtc = tree.DecisionTreeClassifier(max_depth=i)
    dtc.fit(X_train, y_train)
    trains = dtc.score(X_train, y_train)
    tests = dtc.score(X_test, y_test)
    train_score.append(trains)
    test_score.append(tests)
    print(trains, tests)

