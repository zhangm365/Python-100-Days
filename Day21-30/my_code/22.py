
"""
JSON 格式数据
"""

import json

my_dict = {
    'name': 'zhangm365',
    'age': 18,
    'friends': ['Alex', 'Bob'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 300}
    ]
}

print(json.dumps(my_dict))

# 使用 json.dump 函数将字典转为 JSON 格式并写入文本文件。
with open('data.json', 'w') as file:
    json.dump(my_dict, file)


# 将文件对象还原为 Python 对象
with open('data.json', 'r') as file:
    my_dict = json.load(file)
    print(type(my_dict))
    print(my_dict)


"""
使用网络 API 获取数据: 在 python venv 中执行。
"""

import requests
import json

resp = requests.get('https://apis.tianapi.com/guonei/index?key=8cd69cacd1e048d7bdf788d87e37f331&num=10')
if resp.status_code == 200:
    try:
        data_model = resp.json()
        print("\n")
        # print(data_model)  # 查看实际返回的JSON结构
        # 安全访问嵌套结构
        news_list = data_model.get('result', {}).get('newslist', [])
        if not news_list:
            print("未找到新闻数据，请检查API返回内容")
        for news in news_list:
            print(news['title'])
            print(news['url'])
            print('-' * 60)
    except json.JSONDecodeError:
        print("API返回内容非JSON格式，请检查接口有效性")
