"""
元组：不可变容器
"""

# 定义一个三元组
# t1 = (1, 2, 3)
# 明确类型提示以消除类型检查警告
from typing import Tuple, Any

t1: Tuple[int, ...] = (1, 2, 3)

print(t1)
print(type(t1)) # <class 'tuple'>

# t2 = ('zhangm365', 18, True, '广东深圳')
t2: Tuple[Any, ...] = ('zhangm365', 18, True, '广东深圳')

print(t2[-1])

# 切片运算
print(t2[:2])   # ('zhangm365', 18)
print(t2[::3])  # ('zhangm365', '广东深圳')

# 遍历
for elem in t1:
    print(elem)

# 成员运算
print(1 in t1)
print(6 in t1)
print('Hao' not in t2)

# 拼接操作
t3 = t1 + t2  # 现在 t3 的类型为 Tuple[Any, ...]
print(t3)  # (1, 2, 3, 'zhangm365', 18, True, '广东深圳')

# 空元组
a = ()
print(type(a))

b = ('hello')
print(type(b))  # <class 'str'>

c = (100)
print(type(c))  # <class 'int'>

# 一元组：单元素之后需要加上一个逗号
d = ('hello', )
print(type(d))  # <class 'tuple'>
e = (100, )
print(type(e))  # <class 'tuple'>

# 打包和解包操作
a = 1, 10, 100
print(type(a))  # <class 'tuple'>
i, j, k = a
print(i, j, k)

a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)

# 元组是不可变类型，不可变类型适合多线程环境。
# 不可变类型在创建时间上优于对应的可变类型。
import timeit

print('%.3f 秒' % timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]', number=10000000))
print('%.3f 秒' % timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)', number=10000000))

