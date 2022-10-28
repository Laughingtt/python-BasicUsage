import csv  # 处理csv文件
import random  # 用于随机数
import math
import operator


# 加载数据集并分割为训练集和测试集
def loadDataset(filename, split, trainingSet=[], testSet=[]):
    with open(filename, "r") as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)  # 将读入数据转换为列表处理
        for x in range(len(dataset) - 1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                trainingSet.append(dataset[x])
            else:
                testSet.append(dataset[x])


# 计算距离：欧式距离法
def Distance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


# 返回K个最近邻
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance) - 1
    # 计算每一个测试实例到训练集实例的距离
    for x in range(len(trainingSet)):
        dist = Distance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
        # 对所有的距离进行排序
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


# 根据返回的邻居，对其进行分类
def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)  # 按照第一个进行排序
    return sortedVotes[0][0]  # 返回出现次数最多的标签


# 计算准确率
def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct / float(len(testSet))) * 100.0


def main():
    trainingSet = []  # 训练数据集
    testSet = []  # 测试数据集
    split = 0.70  # 分割的比例
    loadDataset(r"iris.data", split, trainingSet, testSet)
    predictions = []
    k = 8
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        result = getResponse(neighbors)
        predictions.append(result)
        print('预测结果:%s,实际结果：%s' % (result, (testSet[x][-1])))
    accuracy = getAccuracy(testSet, predictions)
    print('正确率为: %f' % (accuracy))


if __name__ == "__main__":
    main()