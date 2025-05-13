"""
函数实例
"""


# 1. 随机验证码
import random
import string

ALL_CHARS = string.digits + string.ascii_letters

def generate_code(*, code_len = 4):
    return ''.join(random.choices(ALL_CHARS, k = code_len))

for _ in range(5):
    print(generate_code(code_len = 6))    # 生成 6 个字符的验证码
    # print(generate_code())    # 默认生成 4 个字符的验证码

# 2. 判断是否为素数

def is_prime(num: int) -> bool:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

n = int(input('请输入一个数字：'))
print('它是否为素数：', is_prime(n))

# 3. 两个正整数的最大公约数与最小公倍数

def gcd(x: int, y: int) -> int:
    """最大公约数"""
    while y % x != 0:
        x, y = y % x, x
    return x

print("x 和 y 的最大公约数为：", gcd(int(input('x = ')), int(input('y = '))))

def lcm(x: int, y: int) -> int:
    """最小公倍数"""
    return x * y // gcd(x, y)

print("x 和 y 的最小公倍数为：", lcm(int(input('x = ')), int(input('y = '))))


# 4. 双色球随机选号

import random

RED_BALLS = [i for i in range(1, 34)]
BLUE_BALLS = [i for i in range(1, 17)]

def choose():
    """
    生成一组随机号码
    """
    selected_balls = random.sample(RED_BALLS, 6)
    selected_balls.sort()
    selected_balls.append(random.choice(BLUE_BALLS))
    return selected_balls

def display(balls):
    for ball in balls[:-1]:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    print(f'\033[034m{balls[-1]:0>2d}\033[0m')


n = int(input('生成几注号码：'))
for _ in range(n):
    display(choose())

