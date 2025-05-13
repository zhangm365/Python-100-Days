
"""
函数的高级应用：装饰器
"""

# 1. 装饰器函数
import random
import time

def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')


def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')

## 装饰器：func 是被装饰函数，wrapper 函数是带有装饰功能的函数。
def record_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间：{end - start:.2f}秒')
        return result

    return wrapper


download = record_time(download)    # 直接调用装饰器函数替换原来的函数
upload = record_time(upload)

download('MySQL 从入门到精通.avi')    # 调用
upload('Python 从入门到实践.pdf')

# 2. 装饰器语法糖

@record_time
def download(filename):
    """下载文件"""
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

@record_time
def upload(filename):
    """上传文件"""
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')

print('---------通过装饰器语法糖调用函数：------------')
download('MySQL 从入门到精通.avi')
upload('Python 从入门到实践.pdf')


# 3. 直接调用 functools.wraps 函数
from functools import wraps

def record_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.2f}秒')
        return result

    return wrapper

@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.random() * 6)
    print(f'{filename}下载完成.')

@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.random() * 8)
    print(f'{filename}上传完成.')


## 调用装饰后的函数会记录执行时间
download('MySQL 从入门到精通.avi')
upload('Python 从入门到实践.pdf')
# 取消装饰器的作用不记录执行时间
download.__wrapped__('MySQL 必知必会.pdf')
upload.__wrapped__('Python 从新手到大师.pdf')


# 4. 递归调用
"""
lru_cache 函数是一个带参数的装饰器
"""
from functools import lru_cache

@lru_cache()
def fib1(n):
    if n in (1, 2):
        return 1
    return fib1(n - 1) + fib1(n - 2)


for i in range(1, 51):
    print(fib1(i))
