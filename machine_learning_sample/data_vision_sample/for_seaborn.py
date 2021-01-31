#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/1/31 15:44
# @Author : MarxZhao
# @File : for_seaborn.py
# @Software: PyCharm

import seaborn
import numpy as np
import pandas as pd

mean = 25
sigma = 10

da1 = np.random.normal(mean, sigma, 500).astype(int)
da2 = np.random.normal(mean+5, sigma-4, 500).astype(int)
da3 = np.random.normal(mean-5, sigma+2, 500).astype(int)
dst_data = pd.DataFrame({"A": da1, "B": da2, "C":da3})

data = ["Delhi", "Pune", "Ajmer"]

dst_data['city'] = np.random.choice(data, 500, p=[0.5, 0.2, 0.3]).tolist()

dst_data['gender'] = np.random.choice(['Male', 'Female'], 500, p=[0.6, 0.4]).tolist()

#分布图
seaborn.distplot(da1, bins=10)

#双变量分布
seaborn.jointplot(x=da2, y=da1)

#二元分布的核密度估计
seaborn.jointplot(x=da2, y=da1, kind="kde")

#成对双变量分布
seaborn.pairplot(dst_data)

#分类散点图
seaborn.stripplot(x="city", y="A", data=dst_data, jitter=True)

#小提琴图
seaborn.violinplot(x="B", y="city", data=dst_data)


import matplotlib.pyplot as plt
plt.show()