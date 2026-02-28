"""
使用 NumPy 实现一个朴素贝叶斯分类器：以鸢尾花数据集为例
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, random_state=3)

import numpy as np
import pandas as pd

def naive_bayes_fit(X, y):
    """
    :param X: 样本特征
    :param y: 样本标签
    :returns: 二元组 - (先验概率，似然性)
    """
    # 计算先验概率
    clazz_labels, clazz_counts = np.unique(y, return_counts=True)
    prior_probs = pd.Series({k: v / y.size for k, v in zip(clazz_labels, clazz_counts)})
    # 拷贝数组创建副本
    X = np.copy(X)
    # 保存似然性结果的字典
    likelihoods = {}
    for j in range(X.shape[1]):    # 对特征的循环
        # 对特征进行等宽分箱（离散化处理）
        X[:, j] = pd.cut(X[:, j], bins=5, labels=np.arange(1, 6))
        for i in prior_probs.index:
            # 按标签类别拆分数据并统计每个特征值出现的频次
            x_prime = X[y == i, j]
            x_values, x_counts = np.unique(x_prime,return_counts=True)
            for k, value in enumerate(x_values):    # 对不同特征值的循环
                # 计算似然性并保存在字典中（字典是一个三元组 - (标签，特征序号，特征值)）
                likelihoods[(i, j, value)] = x_counts[k] / x_prime.size
    return prior_probs, likelihoods

p_ci, p_x_ci = naive_bayes_fit(X_train, y_train)
print('先验概率：', p_ci, sep='\n')
print('似然性：', p_x_ci, sep='\n')

def naive_bayes_predict(X, p_ci, p_x_ci):
    """
    朴素贝叶斯分类器预测
    :param X: 样本特征
    :param p_ci: 先验概率
    :param p_x_ci: 似然性
    :return: 预测的标签
    """
    # 对特征进行等宽分箱（离散化处理）
    X = np.copy(X)
    for j in range(X.shape[1]):
        X[:, j] = pd.cut(X[:, j], bins=5, labels=np.arange(1, 6))
    # 保存每个样本对应每个类别后验概率的二维数组
    results = np.zeros((X.shape[0], p_ci.size))
    clazz_labels = p_ci.index.values
    for k in range(X.shape[0]):
        for i, label in enumerate(clazz_labels):
            # 获得先验概率(训练的结果)
            prob = p_ci.loc[label]
            # 计算获得特征数据后的后验概率
            for j in range(X.shape[1]):
                # 如果没有对应的似然性就取值为0
                prob *= p_x_ci.get((i, j, X[k, j]), 0)
            results[k, i] = prob
    # 根据每个样本对应类型最大的概率选择预测标签
    return clazz_labels[results.argmax(axis=1)]

y_pred = naive_bayes_predict(X_test, p_ci, p_x_ci)
print(y_pred == y_test)

"""
使用 scikit-learn 库的 navie_bayes 模块封装的类创建朴素贝叶斯模型。
鸢尾花数据集：它的特征值是连续值，可以用 GaussianNB 来创建模型。
"""
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

from sklearn.metrics import classification_report
print(f'\nsklearn.naive_bayes.GaussianNB 创建的朴素贝叶斯模型:\n', classification_report(y_test, y_pred))

print(model.predict_proba(X_test).round(2))


