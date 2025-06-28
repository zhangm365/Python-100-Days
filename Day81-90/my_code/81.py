
"""
机器学习
"""

import numpy as np

# 每月收入
x = [9558, 8835, 9313, 14990, 5564, 11227, 11806, 10242, 11999, 11630,
        6906, 13850, 7483, 8090, 9465, 9938, 11414, 3200, 10731, 19880,
        15500, 10343, 11100, 10020, 7587, 6120, 5386, 12038, 13360, 10885,
        17010, 9247, 13050, 6691, 7890, 9070, 16899, 8975, 8650, 9100,
        10990, 9184, 4811, 14890, 11313, 12547, 8300, 12400, 9853, 12890]

# 每月网购支出
y = [3171, 2183, 3091, 5928, 182, 4373, 5297, 3788, 5282, 4166,
        1674, 5045, 1617, 1707, 3096, 3407, 4674, 361, 3599, 6584,
        6356, 3859, 4519, 3352, 1634, 1032, 1106, 4951, 5309, 3800,
        5672, 2901, 5439, 1478, 1424, 2777, 5682, 2554, 2117, 2845,
        3867, 2962,  882, 5435, 4174, 4948, 2376, 4987, 3329, 5002]

## 皮尔逊相关系数：两组数据是否存在相关性
print(np.corrcoef(x, y))

"""
kNN 算法
"""
import heapq
import statistics

def predict_by_knn(history_data, param_in, k = 5):
    """
    kNN 算法做预测
    :param history_data: 历史数据
    :param param_in: 输入参数
    :param k: 邻居数量
    :return: 模型的输出（预测结果）
    """

    # 取前 k 个最小数据：key 参数界定最小是指跟输入的参数 param_in 误差最小。
    k_nearest = heapq.nsmallest(k, history_data, key=lambda x: (x - param_in) ** 2)

    # 返回k个最近邻的算术平均值作为预测结果
    return statistics.mean([history_data[item] for item in k_nearest])

incomes = [1800, 3500, 5200, 6600, 13400, 17800, 20000, 30000]
sample_data = {key: value for key, value in zip(x, y)}

for income in incomes:
    print(f'月收入: {income:>5d}元, 月网购支出: {predict_by_knn(sample_data, income):>6.1f}元.')


"""
损失函数：计算均方误差的函数。
"""

def get_loss(X_, y_, a_, b_):
    """损失函数
    :param X_: 回归模型的自变量
    :param y_: 回归模型的因变量
    :param a_: 斜率
    :param b_: 截距
    :return: 均方误差(MSE)
    """

    # y = a * x + b
    y_hat = [a_ * x + b_ for x in X_]
    # v1 和 v2 分别是实际值和预测值
    return statistics.mean([(v1 - v2) ** 2 for v1, v2 in zip(y_, y_hat)])

"""
能让 MSE 达到最小的 a 和 b，我们称回归方程的最小二乘解。
"""

# 使用 numpy 库直接求解 a, b 的值

## 计算样本 x 和 y 的均值
x_bar, y_bar = np.mean(x), np.mean(y)

## np.dot() 函数计算向量的点积
a = np.dot((x - x_bar), (y - y_bar)) / np.sum((x - x_bar) ** 2)
b = y_bar - a * x_bar
print(f'回归方程的最小二乘解：斜率 {a = }, 截距 {b = }')

## 使用 polyfix 函数计算回归方程的最小二乘解
a, b = np.polyfit(x, y, deg=1)    # deg=1 表示线性回归
print(f'回归方程的最小二乘解：斜率 {a = }, 截距 {b = }')

from numpy.polynomial import Polynomial
# 使用 Polynomial 类计算回归方程的最小二乘解
b, a = Polynomial.fit(x, y, deg=1).convert().coef
print(f'回归方程的最小二乘解：斜率 {a}, 截距 {b}')