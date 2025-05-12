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
    print(generate_code())