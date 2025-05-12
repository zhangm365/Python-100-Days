"""
字典操作：每个元素由键值对构成，由分隔符 : 进行划分。
"""

# dict 构造字典
person = dict(name = 'zhangm365', age = 18, height = 180, weight = 75, addr = '广东省深圳市南山区深南大道1号')
print(person)

items1 = dict(zip('ABCDE', '12345'))
print(items1)

items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)

# 使用字典生成式语法创建字典
items3 = {x : x ** 3 for x in range(1, 6)}
print(items3)

# 遍历
person = {
    'name': 'zhangm365',
    'age': 18,
    'height': 180,
    'weight': 75,
    'addr': '深圳市南山区深南大道1号'
}

print('字典 person 的长度为:', len(person))
for key in person:
    print(key)

person = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
    'car': {
        'brand': 'BMW X7',
        'maxSpeed': '250',
        'length': 5170,
        'width': 2000,
        'height': 1835,
        'displacement': 3.0
    }
}
print(person)

# 成员运算
print('name' in person)    # True
print('tel' in person)    # False

# 索引运算
print(person['name'])
print(person['addr'])

person['age'] = 25
person['height'] = 178
person['tel'] = '13906082302'
person['signature'] = '你一定可以！'
print(person)
# 循环遍历
for key in person:
    print(f'{key}:\t{person[key]}')

"""
字典方法
"""
person = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都市武侯区科华北路62号1栋101'}
print(person.get('name'))       # 王大锤
print(person.get('sex'))        # None
print(person.get('sex', True))  # True

person = {'name': '王大锤', 'age': 25, 'height': 178}
print(person.keys())    # dict_keys(['name', 'age', 'height'])
print(person.values())    # dict_values(['王大锤', 25, 178])
print(person.items())    # dict_items([('name', '王大锤'), ('age', 25), ('height', 178)])

"""
字典的应用
"""
sentence = input('请输出一段话：')
counter = {}
for ch in sentence:
    if 'A' <= ch <= 'Z' or 'a' <= ch <= 'z':
        counter[ch] = counter.get(ch, 0) + 1

sorted_keys = sorted(counter, key = counter.get, reverse = True)
for key in sorted_keys:
    print(f'{key} 出现了 {counter[key]} 次.')



