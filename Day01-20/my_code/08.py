
"""
列表: 索引，切片运算等。
"""
items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])
print(items8[-1])
items8[2] = 'durian'
items8[-4] = 'strawberry'
print(items8) # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']

print(items8[0:3:1]) # ['apple', 'strawberry', 'durian']
print(items8[1:5:2]) # ['strawberry', 'peach']
print(items8[-4:-2:1]) # ['strawberry', 'durian']

print(items8[::2]) # ['apple', 'durian', 'watermelon']

print(items8[-2:-6:-1]) # ['peach', 'durian', 'strawberry', 'apple']

"""
列表：遍历
"""
# 1. 通过索引遍历
languages = ['Python', 'Java', 'C++', 'C', 'Go']
for index in range(len(languages)):
    print(index, ':', languages[index])


#  2. 直接对列表进行循环
for language in languages:
    print(language)


"""
统计骰子的出现次数
"""
import random

counter = [0] * 6
for _ in range(6000):
    point = random.randrange(1, 7)
    counter[point - 1] += 1

for point in range(1, 7):
    print(f'点数{point}出现的次数为：{counter[point - 1]}次')