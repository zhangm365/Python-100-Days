
"""
决策树
"""

import numpy as np

def entropy(y):
    """
    计算信息熵
    :param y: 数据集的目标值
    :return: 信息熵
    """
    _, counts = np.unique(y, return_counts = True)
    prob = counts / y.size
    return -np.sum(prob * np.log2(prob))


