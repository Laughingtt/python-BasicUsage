import numpy as np
import h5py
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, roc_curve


def load_data():
    all_data = pd.read_csv("wcdata.csv")
    X_data = all_data.iloc[:, 2:]
    X = np.array(X_data)
    y = all_data['is_bad']
    y = np.array(y)
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    # y_train = y_train.reshape(y_train.shape[0], 1)
    # y_test = y_test.reshape(y_test.shape[0], 1)
    return x_train, x_test, y_train, y_test


# y ([1,1,1,0,0,1])
x_train, x_test, y_train, y_test = load_data()
logistic = LogisticRegression()
logistic.fit(x_train, y_train)
score = logistic.score(x_test, y_test)

y_pre = logistic.predict_proba(x_test)
y_0 = list(y_pre[:, 1])  # 取第二列数据，因为第二列概率为趋于0时分类类别为0，概率趋于1时分类类别为1

fpr, tpr, thresholds = roc_curve(y_test, y_0)  # 计算fpr,tpr,thresholds
auc = roc_auc_score(y_test, y_0)  # 计算auc

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

print("sklearn---run")
print("模型得分:",score)
print('auc为：', auc)
print('最大KS为：', KS_max)
print('最佳阈值为：', best_thr)

# 画曲线图
plt.figure()
plt.plot(fpr, tpr)
plt.title('$ROC curve$')
plt.show()