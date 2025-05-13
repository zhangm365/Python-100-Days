"""
函数的进阶用法
"""

def calc(*args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = 0
    for item in items:
        if type(item) in (int, float):
            result += item
    return result


print(calc(1, 2, 3, a = 4.5, b = 5.6))


# 1. 函数作为函数参数使用

def calc(init_val, op_func, *args, **kwargs):
    items = list(args) + list(kwargs.values())
    result = init_val
    for item in items:
        if type(item) in (int, float):
            result = op_func(result, item)

    return result

def add(x, y):
    return x + y

def mul(x, y):
    return x * y

print(calc(0, add, 1, 2, 3, 4, 5))
print(calc(1, mul, 1, 2, 3, a = 4, b = 5))

# 2. sorted 函数：返回一个新的列表，不会修改原始列表

old_strings = ['in', 'apple', 'zoo', 'banana', 'pear']
new_strings = sorted(old_strings)
print(new_strings)

## 按字符串长度排序，而不是按字母表顺序排序
new_strings = sorted(old_strings, key = len)
print(new_strings)

# 3. list.sort: 会直接修改原始列表
old_strings.sort()
print(old_strings)

