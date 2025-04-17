
import math

r = float(input("请输入半径："))
per = 2 * math.pi * r
area = math.pi * r * r
print(f'周长：{per = :.2f}')
print(f'面积：{area = :.2f}')

year = int(input("请输入年份："))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} 是闰年')
else:
    print(f'{year} 不是闰年')