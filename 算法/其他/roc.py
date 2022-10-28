#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:roc.py
@time:2020/12/03

"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

ture_y = np.array([1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0])

np.random.seed(1)
predict_y = np.random.rand(len(ture_y))
print(predict_y)
fpr, tpr, thresholds = roc_curve(ture_y, predict_y)
auc_value = auc(fpr, tpr)

ks = max(tpr-fpr)

print("fpr:{},tpr:{}".format(fpr,tpr))
print("thresholds:{}".format(thresholds))
plt.plot(fpr, tpr)
plt.legend(["auc:%.2f ks:%d"%(auc_value,ks*100)])
plt.show()

