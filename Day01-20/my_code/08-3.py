
"""
列表中元素的方法
"""

# 1. index, count 方法
items = ['Python', 'Java', 'C++', 'Python']
print(items.index('Python'))    # 返回第一个元素的索引
# 从索引 1 开始查找 'Python'
print(items.index('Python', 1)) # 3
print(items.count('Python'))    # 2
# print(items.index('C', 1))  # ValueError: 'C' is not in list

# 2. 排序与反转
items = ['Python', 'Java', 'C++', 'Go']
items.sort()
print(items)
items.reverse()
print(items)

# 3. 列表生成式: 强烈建议使用此语法创建列表
nums1 = [35, 12, 97, 64, 55]
nums2 = [num for num in nums1 if num > 50]
print(nums2)

import random
scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
print(scores)

"""
双色球随机选号程序
"""
import random
red_balls = list(range(1, 34))
select_balls = []
for _ in range(6):
    index = random.randrange(len(red_balls))
    select_balls.append(red_balls.pop(index))
# 排序
select_balls.sort()
# 输出选中的红色球
for ball in select_balls:
    print(f'\033[031m{ball:0>2d}\033[0m', end=' ')

blue_ball = random.randrange(1, 17)
print(f'\033[034m{blue_ball:0>2d}\033[0m')

"""
随机生成 N 注号码
"""
import random
n = int(input('生成几注号码：'))
red_balls = list(range(1, 34))
blue_balls = list(range(1, 17))

for _ in range(n):
    select_balls = random.sample(red_balls, 6)  # 无放回随机抽样
    select_balls.sort()
    for ball in select_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')

    blue_ball = random.choice(blue_balls)   # 随机抽取一个元素
    print(f'\033[034m{blue_ball:0>2d}\033[0m')


"""
双色球随机选号程序

Author: zhangm365
Version: 1.3
"""
import random

from rich.console import Console
from rich.table import Table

# 创建控制台
console = Console()

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]

# 创建表格并添加表头
table = Table(show_header=True)
for col_name in ('序号', '红球', '蓝球'):
    table.add_column(col_name, justify='center')

for i in range(n):
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    blue_ball = random.choice(blue_balls)
    # 向表格中添加行（序号，红色球，蓝色球）
    table.add_row(
        str(i + 1),
        f'[red]{" ".join([f"{ball:0>2d}" for ball in selected_balls])}[/red]',
        f'[blue]{blue_ball:0>2d}[/blue]'
    )

# 通过控制台输出表格
console.print(table)
