
"""
决策树
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def entropy(y):
    """
    计算信息熵
    :param y: 数据集的目标值
    :return: 信息熵
    """
    _, counts = np.unique(y, return_counts=True)
    prob = counts / y.size
    return -np.sum(prob * np.log2(prob))

def info_gain(x, y):
    """
    计算信息增益
    :param x: 给定的特征
    :param y: 数据集的目标值
    :return: 信息增益
    """

    values, counts = np.unique(x, return_counts=True)
    new_entropy = 0
    for i, value in enumerate(values):
        prob = counts[i] / x.size
        new_entropy += prob * entropy(y[x == value])
    return entropy(y) - new_entropy

def info_gain_ratio(x, y):
    """
    计算信息增益比
    :param x: 给定的特征
    :param y: 数据集的目标值
    :return: 信息增益比
    """
    return info_gain(x, y)/entropy(x)

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=3)

print(f'H(D) = {entropy(y_train)}')
print(f'g(D,A0) = {info_gain(X_train[:, 0], y_train)}')
print(f'g(D,A1) = {info_gain(X_train[:, 1], y_train)}')
print(f'g(D,A2) = {info_gain(X_train[:, 2], y_train)}')
print(f'g(D,A3) = {info_gain(X_train[:, 3], y_train)}')

print(f'R(D,A0) = {info_gain_ratio(X_train[:, 0], y_train)}')
print(f'R(D,A1) = {info_gain_ratio(X_train[:, 0], y_train)}')
print(f'R(D,A2) = {info_gain_ratio(X_train[:, 0], y_train)}')
print(f'R(D,A3) = {info_gain_ratio(X_train[:, 0], y_train)}')
