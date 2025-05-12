"""
函数
"""
from math import factorial


# 阶乘
def fac(num):
    result = 1
    for ele in range(2, num + 1):
        result *= ele

    return result

m = int(input('m = '))
n = int(input('n = '))

print(fac(m) // fac(n) // fac(m - n))

# 使用 python 标准库 math 模块实现的 factorial 求阶乘

print('调用 math 模块的 factorial 函数:')
from math import factorial
m = int(input('m = '))
n = int(input('n = '))
print(factorial(m) // factorial(n) // factorial(m - n))

def make_judgement(*, a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b

print(make_judgement(a = 4, b = 5, c = 6))

# 星号表达式表示函数支持可变参数：函数接受 0 个或任意个参数
def add(*args):
    total = 0
    for val in args:
        if type(val) in (int, float):
            total += val

    return total

print(add())
print(add(1))
print(add(1, 2, 3))
print(add(1, 2, 'hello', 3.45, 6))

# 关键字参数
def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo(3, 2.1, True, name = 'zhangm365', age = 18, gpa = 4.95)
# (3, 2.1, True)
# {'name': 'zhangm365', 'age': 18, 'gpa': 4.95}

