"""
列表的方法函数
"""

languages = ['Python', 'Java', 'C++', 'Python']
languages.append('JavaScript')
print(languages)  # ['Python', 'Java', 'C++', 'Python', 'JavaScript']
languages.insert(1, 'SQL')
print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'Python', 'JavaScript']

if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift') # 如果直接删除不存在的元素将报错：ValueError

if 'Python' in languages:
    languages.remove('Python')  # 如果存在多个元素，则仅删除匹配到第一个元素。

print(languages)  # ['SQL', 'C++', 'Python', 'JavaScript']

temp = languages.pop()  # pop 删除并返回列表中指定索引的元素，弹出的元素可以继续使用。
print(temp)
languages.append(temp)
print(languages)

temp = languages.pop(0)
print(temp)
languages.append(temp)
print(languages)

languages.clear()   # 清空列表
print(languages)

items = ['Python', 'Java', 'C++']
del items[0]
print(items)


