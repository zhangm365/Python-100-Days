
"""
scikit-learn 机器学习库
"""

import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
from scipy import stats

# 1. 加载数据集
## 加载鸢尾花数据集
iris = load_iris()
# 查看数据集的介绍
# print(iris.DESCR)

X = iris.data  # 特征数据（150 行 4 列的二维数据，分别是花萼长，花萼宽，花瓣长，花瓣宽）
y = iris.target  # 标签（150 个元素的一维数组，包括 0,1,2 三个值表示三种鸢尾花）

# 将数据集转换为 DataFrame
df = pd.DataFrame(X, columns=iris.feature_names)
df['target'] = y
df['species'] = pd.Categorical.from_codes(y, iris.target_names)
print(df.head())  # 打印前几行数据

# 2. 数据集的划分
"""
将原始数据集划分为训练集和测试集
"""

# 将特征和标签堆叠到同一个数组中
data = np.hstack((X, y.reshape(-1, 1)))
print(data.shape)  # 打印数据集的形状

np.random.shuffle(data)  # 打乱数据集顺序

# 划分训练集和测试集
train_size = int(0.8 * y.size)  # 80% 用于训练
train, test = data[:train_size], data[train_size:]

## 训练集特征：所有行，所有列（除了最后一列）
X_train = train[:, :-1]

## 训练集标签：所有行，最后一列
y_train = train[:, -1]

X_test = test[:, :-1]
y_test = test[:, -1]

"""
3. kNN 分类的实现
"""
# 1. 基于 Numpy 的实现

def euclidean_distance(u, v):
    """计算两个 n 维向量的欧氏距离"""
    return np.sqrt(np.sum((u - v) ** 2))


# 根据邻居的标签为新数据生成标签
def make_label(X_train, y_train, X_one, k):
    """
    根据历史数据中 k 个最近邻为新数据生成标签
    :param X_train: 训练集特征
    :param y_train: 训练集标签
    :param X_one: 新数据特征
    :param k: 最近邻的个数
    :return: 为待测样本生成的标签
    """

    distes = [euclidean_distance(X_one, X_i) for X_i in X_train]  # 计算新数据与训练集中每个样本的距离
    # 通过一次划分找到 k 个最小距离对应的索引并获取到相应的标签
    labels = y_train[np.argpartition(distes, k - 1)[:k]]
    # 获取标签的众数
    return stats.mode(labels).mode

def predict_by_knn(X_train, y_train, X_new, k=5):
    """
    基于 kNN 算法对新数据进行预测
    :param X_train: 训练集特征
    :param y_train: 训练集标签
    :param X_new: 待预测样本组成的数组
    :param k: 最近邻的个数(默认为 5)
    :return: 保存预测结果的数组
    """
    return np.array([make_label(X_train, y_train, X, k) for X in X_new])

# 使用 kNN 预测的 30 条鸢尾花的标签
y_pred = predict_by_knn(X_train, y_train, X_test)  # 对测试集进行预测
print(f'预测结果：{y_pred}')
# 比较预测标签和实际标签
print(y_pred == y_test)