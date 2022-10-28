import numpy as np
import h5py
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, roc_curve


def load_data():
    all_data = pd.read_csv("wcdata.csv")
    X_data = all_data.iloc[:, 2:]
    X = np.array(X_data)
    y = all_data['is_bad']
    y = np.array(y)
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    y_train = y_train.reshape(y_train.shape[0], 1)
    y_test = y_test.reshape(y_test.shape[0], 1)
    return x_train, x_test, y_train, y_test


def init_params(x_train):
    ##初始化w,和b
    w = np.zeros((1, x_train.shape[1]))
    # b是一个偏置初始化一个就行
    b = 0

    params = {
        "w": w,
        "b": b,
    }

    return params


def sigmod(z):
    s = 1 / (1 + np.exp(-z))
    return s


def forward_propagation(x_train, y_train, w, b):
    m = x_train.shape[0]
    """正向传播"""
    # 计算Z值
    Z = np.dot(x_train, w.T) + b  # (m,1)

    # 计算A激活函数后的A
    A = sigmod(Z)  # (m,1)
    # 计算出成本
    cost = (-1 / m) * np.sum(y_train * np.log(A) + (1 - y_train) * (np.log(1 - A)))

    cost = np.squeeze(cost)
    # print("Z", A)
    """反向传播"""
    # 计算dz->然后计算dw和db

    # 转置矩阵相乘为(209,1)
    dz = A - y_train  # (m,1)

    dw = (1 / m) * np.dot(x_train.T, dz)  # (x,1)
    dw = dw.T  # (1,x)
    db = (1 / m) * np.sum(dz)  # 常数

    params = {
        "cost": cost,
        "dw": dw,
        "db": db,
        "w": w,
        "b": b
    }
    return params


def update_params(x_train, y_train, para, loop=2000, learnning_rate=0.01):
    """
    根据学习率更新参数w,和b ,学习率应设置在0.001左右，学习率过大就不会收敛,得根据当前数据情况来调试合适得学习率
    """

    costs = []

    w = para['w']
    b = para['b']

    for i in range(int(loop)):
        para = forward_propagation(x_train, y_train, w, b)
        cost = para['cost']
        dw = para['dw']
        db = para['db']
        w = para['w']
        b = para['b']

        w = w - learnning_rate * dw
        b = b - learnning_rate * db
        if i % 100 == 0:
            print("第%s次循环,成本等于%s" % (str(i), str(cost)))
            costs.append(cost)

    params = {
        "w": w,
        "b": b}
    grads = {
        "dw": dw,
        "db": db}

    return params, grads, costs


def predict(X, params):
    w = params['w']
    b = params['b']
    m = X.shape[0]
    """正向传播"""
    # 计算Z值
    Z = np.dot(X, w.T) + b  # (m,1)
    Y_prediction = np.zeros((m, 1))

    # 计算A激活函数后的A
    A = sigmod(Z)  # (m,1)

    for i in range(A.shape[0]):
        # 将概率a [0，i]转换为实际预测p [0，i]
        Y_prediction[i, 0] = 1 if A[i, 0] > 0.5 else 0

    return Y_prediction, A


def ks_value(fpr, tpr, thresholds):
    # 计算ks
    KS_max = 0
    best_thr = 0
    for i in range(len(fpr)):
        if (i == 0):
            KS_max = tpr[i] - fpr[i]
            best_thr = thresholds[i]
        elif (tpr[i] - fpr[i] > KS_max):
            KS_max = tpr[i] - fpr[i]
            best_thr = thresholds[i]

    print('最大KS为：', KS_max)
    print('最佳阈值为：', best_thr)
    return KS_max, best_thr


def auc_ghaph(y_test, predict_test_A, fpr, tpr):
    auc = roc_auc_score(y_test, predict_test_A)  # 计算auc
    print('auc值为：', auc)
    # 画曲线图
    plt.figure()
    plt.plot(fpr, tpr)
    plt.title('$ROC curve$')
    # plt.show()
    plt.savefig('./auc.pdf')
    plt.close()
    return auc


def model():
    # x代表特征值数量 m代表样本数量
    # x (m,x)
    # y (m,1)
    # w (1,x)
    # b 常数
    # Z (m,1)
    # A (m,1)
    # dz (m,1)
    # dw #(x,1) --(1,x) 用于更新参数
    # db 常数

    # 加载数据
    x_train, x_test, y_train, y_test = load_data()

    # 初始化参数
    para = init_params(x_train)

    # 更新参数
    params, grads, costs = update_params(x_train, y_train, para, loop=2000, learnning_rate=0.01)

    # 预测
    predict_train_y, predict_train_A = predict(x_train, params)
    predict_test_y, predict_test_A = predict(x_test, params)

    # 打印训练后的准确性
    # 当预测值与实际值一样时，值为零；预测值不准确时值为1，所以对为1的值求平均，就是不准确率
    print("训练集准确性：", format(100 - np.mean(np.abs(predict_train_y - y_train)) * 100), "%")
    print("测试集准确性：", format(100 - np.mean(np.abs(predict_test_y - y_test)) * 100), "%")

    # 计算fpr,tpr,ks,auc
    fpr, tpr, thresholds = roc_curve(y_test, predict_test_A)  # 计算fpr,tpr,thresholds
    ks = ks_value(fpr, tpr, thresholds)
    auc = auc_ghaph(y_test, predict_test_A, fpr, tpr)

    return costs, ks, auc


if __name__ == '__main__':
    costs, ks, auc = model()
    # 绘制学习过程图
    # squeeze 函数：从数组的形状中删除单维度条目，即把shape中为1的维度去掉
    costs = np.squeeze(costs)
    plt.plot(costs)
    plt.ylabel('cost')
    plt.xlabel('iterations (per hundreds)')
    plt.title("Learning rate =" + str(0.01))
    plt.show()
