
"""
Python 进阶编程
"""

# 1. 生成式语法
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

## 1. 将股票价格大于  100 的股票构造一个新字典
new_prices = {key: value for key, value in prices.items() if value > 100}

print(new_prices)

# 2. 嵌套列表

names = ['关羽', '张飞', '赵云', '马超', '黄忠']
courses = ['语文', '数学', '英语']

scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#     print(scores[row])
#     print()


# 3. 堆排序

import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(heapq.nlargest(3, list1))
print(heapq.nsmallest(3, list1))
print(heapq.nlargest(2, list2, key = lambda x: x['price']))
print(heapq.nsmallest(2, list2, key = lambda x: x['shares']))


# 4. 迭代器模块：itertools 模块
import itertools

print(list(itertools.permutations('ABCD')))  # 将生成器转换为列表后输出
print(list(itertools.combinations('ABCDE', 3)))
print(list(itertools.product('ABCD', '123')))
# print(list(itertools.cycle(('A', 'B', 'C'))))

# 5. 容器数据类型：collections 模块

## Counter: dict 的子类，键是元素，值是元素的计数。
from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]
counter = Counter(words)
print("\nCollections.Counter usage: ")
print(counter.most_common(3))

# 6. 排序算法

def select_sort(items, comp = lambda x, y: x < y):
    """
    简单选择排序
    该算法是一个不稳定算法。
    """
    # 拷贝
    items = items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):    # 在「未排序」序列中找到一个最小的元素
            if comp(items[j], items[min_index]):
                min_index = j

        items[i], items[min_index] = items[min_index], items[i]

    return items

## 自定义排序对象
class Data:
    def __init__(self, num, ch):
        self.num = num
        self.ch = ch
    def __repr__(self):
        return f"Data({self.num}, '{self.ch}')"

data = [Data(2, 'a'), Data(3, 'b'), Data(2, 'c'), Data(1, 'd')]
data_sorted = select_sort(data, lambda x, y: x.num < y.num)
print(f'简单选择排序的结果：{data_sorted}')

def bubble_sort(items, comp = lambda x, y: x > y):
    """冒泡排序"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if not swapped:
            break

    return items


data = [3, 2, 1, 4, 5, 8]
data_sorted = bubble_sort(data)
print(f'冒泡排序的结果：{data_sorted}')

def bubble_sort_opt(items, comp = lambda x, y: x > y):
    """搅拌排序(冒泡排序升级版: 双向排序)"""
    items = items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(len(items) - 1 - i):    # 正向遍历
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True

        if swapped:    ## 反向遍历
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True

        if not swapped:
            break

    return items

data = [3, 2, 1, 4, 5, 8]
data_sorted = bubble_sort_opt(data)
print(f'升级版冒泡排序的结果：{data_sorted}')


def merge(items1, items2, comp = lambda x, y: x < y):
    """合并(将两个有序的列表合并成一个有序的列表)"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1

    items += items1[index1:]
    items += items2[index2:]
    return items


# 主函数调用
def merge_sort(items, comp = lambda x, y: x < y):
    return _merge_sort(list(items), comp)


def _merge_sort(items, comp):
    """归并排序"""
    if len(items) < 2:
        return items

    mid = len(items) // 2
    left = _merge_sort(items[:mid], comp)
    right = _merge_sort(items[mid:], comp)
    return merge(left, right, comp)


data1 = [2, 3, 5, 6, 0]
data2 = [4, 5, 10, 8, 1]
data1_sort = merge_sort(data1)
data2_sort = merge_sort(data2)

print(f'归并排序的结果：{data1_sort}')
print(f'归并排序的结果：{data2_sort}')


# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(f'公鸡数量 = {x}, 母鸡数量 = {y}, 小鸡数量 = {z}')

# 五人合伙捕鱼
fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5


#
class Thing(object):
    """物品"""

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight

def input_thing():
    """请输入物品信息"""
    # 添加输入提示，说明输入格式为：名称 价格 重量
    print("请输入物品名称、价格、重量（用空格分隔）：")
    name_str, price_str, weight_str = input().split()
    return name_str, int(price_str), int(weight_str)

def main():
    """主函数"""
    # 添加输入提示，说明输入格式为：最大承重 物品数量
    print("请输入背包最大承重和物品数量（用空格分隔）：")
    max_weight, num_of_things = map(int, input().split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))    # 解包传参

    all_things.sort(key=lambda t: t.value, reverse=True)
    total_weight = 0
    total_price = 0
    for thing in all_things:
        if total_weight + thing.weight <= max_weight:
            print(f'小偷偷走了{thing.name}')
            total_weight += thing.weight
            total_price += thing.price

    print(f'总价值：{total_price} 美元')

if __name__ == '__main__':
    main()
