"""
Python 读写 CSV 文件
"""

# 1. 将数据写入 CSV 文件
import csv
import random

with open('scores.csv', 'w') as file:
    # writer = csv.writer(file)
    writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)
    writer.writerow(['姓名', '语文', '数学', '英语'])
    names = ['张三', '李四', '王五', '赵六']
    for name in names:
        scores = [random.randrange(70, 101) for _ in range(3)]
        row = [name] + scores
        writer.writerow(row)

# 2. 从 CSV 文件中读取数据

import csv

with open('scores.csv', 'r') as file:
    reader = csv.reader(file, delimiter='|')
    for data_list in reader:    # 每次从 reader 对象取出一个列表对象
        print(reader.line_num, end='\t')
        for elem in data_list:
            print(elem, end='\t')
        print()