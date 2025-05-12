"""
集合操作
"""

set1 = {1, 2, 3, 3, 3, 4, 5}
print(set1)    # {1, 2, 3, 4, 5}

set2 = set("hello")
print(set2)    # 输出内容是随机(无序)的：{'l', 'h', 'o', 'e'}

set3 = set([1, 2, 2, 3, 3, 3, 2, 1])    # 生成式语法
print(set3)

set4 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set4)

# 遍历元素
set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Go'}
for elem in set1:
    print(elem)

""" 
二元运算: 集合的交集、并集、差集、对称差等运算。
"""
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}

# 交集
print("两个集合的交集为：")
print(set1 & set2)    # {2, 4, 6}
print(set1.intersection(set2))

# 并集
print("两个集合的并集为：")
print(set1 | set2)    # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1.union(set2))

# 差集
print("两个集合的差集为：")
print(set1 - set2)    # {1, 3, 5, 7}
print(set1.difference(set2))

print("两个集合的对称差为：")
print(set1 ^ set2)    # {1, 3, 5, 7, 8, 10}
print(set1.symmetric_difference(set2))

set1 = {1, 3, 5, 7}
set2 = {2, 4, 6}
set1 |= set2
# set1.update(set2)
print(set1)    # {1, 2, 3, 4, 5, 6, 7}

set3 = {3, 6, 9}
set1 &= set3
# set1.intersection_update(set3)
print(set1)  # {3, 6}

set2 -= set1
# set2.difference_update(set1)
print(set2)  # {2, 4}

set1.clear()
print(set1)    # set()

