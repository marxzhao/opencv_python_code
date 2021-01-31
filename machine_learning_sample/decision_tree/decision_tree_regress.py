#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/17 17:37
# @Author : MarxZhao
# @File : decision_tree_regress.py
# @Software: PyCharm


from sklearn import datasets
import sklearn.model_selection as ms
from sklearn import tree
import numpy as np
rng = np.random.RandomState(42)

x = np.sort(5 * rng.rand(100, 1), axis=0)
y = np.sin(x).ravel()
y[::2] += 0.5 * (0.5 - rng.rand(50))

dtc = tree.DecisionTreeRegressor(max_depth=2, random_state=42)
dtc.fit(x, y)
tree.DecisionTreeClassifier(criterion='mse',
                            max_depth=2, max_features=None,
                            max_leaf_nodes=None,
                            min_impurity_split=1e-07,
                            min_samples_leaf=1,
                            min_samples_split=2, random_state=42,
                            splitter='best')

X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_test = dtc.predict(X_test)
print(y_test)

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.scatter(x, y, c='k', s=50, label='data')
plt.plot(X_test, y_test, label="max_depth=2", linewidth=5)
plt.xlabel("data")
plt.ylabel("target")
plt.legend()
plt.show()
