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

# 3. 最大公约数与最小公倍数

def gcd(x: int, y: int) -> int:
    if x == 0:
        return y
    while y % x != 0:
        x, y = y % x, x
    return x

print("x 和 y 的最大公约数为：", gcd(int(input('x = ')), int(input('y = '))))

def lcm(x: int, y: int) -> int:
    return x * y // gcd(x, y)

print("x 和 y 的最小公倍数为：", lcm(int(input('x = ')), int(input('y = '))))
