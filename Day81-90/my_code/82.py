
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
df = pd.DataFrame(X, columns=iris.feature_names)    # 特征数据
df['target'] = y    # 标签
df['species'] = pd.Categorical.from_codes(y, iris.target_names)
print(df.head())  # 打印前几行数据

# 2. 数据集的划分
"""
将原始数据集划分为训练集和测试集
"""

# 将特征和标签堆叠到同一个数组中
data = np.hstack((X, y.reshape(-1, 1)))    # (150, 5) 的二维数组
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


## 3.1 基于 scikit-learn 的实现

from sklearn.neighbors import KNeighborsClassifier

# 创建模型
model = KNeighborsClassifier()

# 训练模型
model.fit(X_train, y_train)

y_pred = model.predict(X_test)  # 对测试集进行预测
print(y_pred == y_test)

print(model.score(X_test, y_test))  # 计算模型的准确率


## scikit-learn 混淆矩阵和评估报告

from sklearn.metrics import confusion_matrix, classification_report
print('混淆矩阵：')
print(confusion_matrix(y_test, y_pred))  # 混淆矩阵
print('分类报告：')
print(classification_report(y_test, y_pred))

# 4. 可视化结果
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

cm_display_obj = ConfusionMatrixDisplay(confusion_matrix(y_test, y_pred), display_labels=iris.target_names)

cm_display_obj.plot(cmap=plt.cm.Reds)
plt.show()

from sklearn.metrics import roc_curve, auc
from sklearn.metrics import RocCurveDisplay

# 手动构造一组真实值和对应的预测值
y_test_ex = np.array([0, 0, 0, 1, 1, 0, 1, 1, 1, 0])
y_pred_ex = np.array([1, 0, 0, 1, 1, 0, 1, 1, 0, 1])

# 通过 roc_curve 计算 FPR（假正例率） 和 TPR（真正例率）
fpr, tpr, _ = roc_curve(y_test_ex, y_pred_ex)
# 通过 auc 函数计算出 AUC 值并通过 RocCurveDisplay 绘制 ROC 曲线
RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=auc(fpr, tpr)).plot()
plt.show()


from sklearn.model_selection import GridSearchCV

gs = GridSearchCV(
    estimator=KNeighborsClassifier(),
    param_grid={
        'n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15],
        'weights': ['uniform', 'distance'],
        'p': [1, 2]  # 1 表示曼哈顿距离，2 表示欧氏距离
    },
    cv=5
)

gs.fit(X_train, y_train)

print(f'最佳参数：{gs.best_params_}')
print(f'得分：{gs.best_score_}')

gs.predict(X_test)  # 使用最佳参数进行预测


"""
kNN 回归
"""

# 每月收入
incomes = np.array([
    9558, 8835, 9313, 14990, 5564, 11227, 11806, 10242, 11999, 11630,
    6906, 13850, 7483, 8090, 9465, 9938, 11414, 3200, 10731, 19880,
    15500, 10343, 11100, 10020, 7587, 6120, 5386, 12038, 13360, 10885,
    17010, 9247, 13050, 6691, 7890, 9070, 16899, 8975, 8650, 9100,
    10990, 9184, 4811, 14890, 11313, 12547, 8300, 12400, 9853, 12890
])
# 每月网购支出
outcomes = np.array([
    3171, 2183, 3091, 5928, 182, 4373, 5297, 3788, 5282, 4166,
    1674, 5045, 1617, 1707, 3096, 3407, 4674, 361, 3599, 6584,
    6356, 3859, 4519, 3352, 1634, 1032, 1106, 4951, 5309, 3800,
    5672, 2901, 5439, 1478, 1424, 2777, 5682, 2554, 2117, 2845,
    3867, 2962,  882, 5435, 4174, 4948, 2376, 4987, 3329, 5002
])

X = np.sort(incomes).reshape(-1, 1)  # 将收入排序后处理成二维数组
y = outcomes[np.argsort(incomes)]    # 将网购支出按照收入进行排序

from sklearn.neighbors import KNeighborsRegressor

model = KNeighborsRegressor()
model.fit(X, y)
y_pred = model.predict(X)

# 原始数据散点图
plt.scatter(X, y, color='navy')
# 预测结果折线图
plt.plot(X, y_pred, color='coral')
plt.show()

