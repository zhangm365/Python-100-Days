
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
