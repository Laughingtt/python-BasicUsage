#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:手写逻辑回归.py
@time:2021/04/08

"""
import matplotlib

matplotlib.use('TkAgg')
import copy
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics




def load_data():
    data = pd.read_csv("/Users/tian/Projects/python-BasicUsage/算法/data/my_data_guest.csv")
    y = data["bad"]
    X = data.iloc[:, 2:]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    return X_train.values, X_test.values, y_train.values.reshape(-1, 1), y_test.values.reshape(-1, 1)


X_train, X_test, y_train, y_test = load_data()


def init_params(dim):
    w = np.zeros(shape=(dim, 1))
    b = 0
    return w, b


def sigmoid(z):
    """
    参数：
        z  - 任何大小的标量或numpy数组。

    返回：
        s  -  sigmoid（z）
    """
    s = 1 / (1 + np.exp(-z))
    return s


def train(loop=1000, learning_rate=0.1):
    """
    1.Z = wT * X + b
    2.A = Sigmoid（Z）
    3.Cost = -(Y * Log(A) + (1-Y) * Log(1-A)) / m  =  (-Y * Z + Log(1 + eZ)) / m      （m是样本的数量）
    4.dw = X * (A – Y)T / m
    5.db = (A – Y) / m
    6.w = w – alpha * dw     (alpha是学习率)
    7.b = b – alpha * db
    """
    costs = []
    m = X_train.shape[0]
    w, b = init_params(X_train.shape[1])

    for i in range(loop):
        # w (dim,1) x (1000,dim)
        Z = np.dot(X_train, w).reshape(-1, 1)

        A = sigmoid(Z)
        dz = (A - y_train)  # (700,1)

        loss = -(1 / m) * np.sum(y_train * np.log(A) + (1 - y_train) * np.log(1 - A))

        dw = (1 / m) * np.dot(dz.T, X_train)  # (1,12)
        db = (1 / m) * np.sum(dz)

        w = w - learning_rate * dw.T
        b = b - learning_rate * db

        costs.append(loss)

    params = {
        "w": w,
        "b": b,
        "costs": costs
    }
    return params


def predict(params, X):
    Z = np.dot(X, params["w"]).reshape(-1, 1)

    predict_train_y = sigmoid(Z)
    predict_train_pre = copy.deepcopy(predict_train_y)

    for i in range(predict_train_y.shape[0]):
        predict_train_y[i, 0] = 1 if predict_train_y[i, 0] > 0.5 else 0
    return predict_train_y, predict_train_pre


def drow_loss(params):
    plt.plot(params["costs"])
    plt.ylabel('cost')
    plt.xlabel('iterations')
    plt.title("Learning rate =" + str(0.001))
    plt.show()


params = train()

predict_train_y, predict_train_pre = predict(params, X_train)
predict_test_y, predict_test_pre = predict(params, X_test)
print("训练集准确性：", format(100 - np.mean(np.abs(predict_train_y - y_train)) * 100), "%")
print("测试集准确性：", format(100 - np.mean(np.abs(predict_test_y - y_test)) * 100), "%")

fpr, tpr, thresholds = metrics.roc_curve(y_train.flatten(), predict_train_pre.flatten())
auc = metrics.auc(fpr, tpr)
print(auc)

drow_loss(params)
