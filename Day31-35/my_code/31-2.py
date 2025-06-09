"""
并发编程
"""

import glob
import os
import threading
from concurrent.futures import ThreadPoolExecutor

from PIL import Image

PREFIX = "thumbnails"

def generate_thumbnail(infile, size, format='PNG'):
    """生成指定图片的缩略图"""
    try:
        # 路径处理
        filename = os.path.basename(infile)
        name, ext = os.path.splitext(filename)

        # 输出目录
        os.makedirs(PREFIX, exist_ok = True)
        outfile = os.path.join(PREFIX, f'{name}_{size[0]}_{size[1]}{ext}')

        with Image.open(infile) as img:
            if not (isinstance(size, (tuple, list)) and len(size) == 2):
                raise ValueError("size 参数必须是包含两个整数的元组")

            img.thumbnail(size, Image.Resampling.LANCZOS)
            img.save(outfile, format=format)

        return True

    except FileNotFoundError:
        print(f"错误：文件{infile}不存在")
        return False
    except Image.UnidentifiedImageError:
        print(f"错误：无法识别的图片格式 - {infile}")
        return False
    except Exception as e:
        print(f"处理文件 {infile} 时发生未知错误：{str(e)}")
        return False


def main():
    """主函数"""
    ## 线程池
    with ThreadPoolExecutor(max_workers=5) as executor:
        tasks = [
            executor.submit(generate_thumbnail, infile, (size, size))
            for infile in glob.glob('images/*.png')
            for size in (32, 64, 128)
        ]


if __name__ == '__main__':
    main()


# 2. 多线程的资源竞争

import threading
import time

from concurrent.futures import ThreadPoolExecutor

class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, money):
        """通过锁保护临界资源"""
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance

def main():
    account = Account()
    futures = []
    # 创建线程池
    with ThreadPoolExecutor(max_workers=10) as executor:

        for _ in range(100):
            future = executor.submit(account.deposit, 1)
            futures.append(future)

    for future in futures:
        future.result()  # 等待所有任务执行完成

    print(account.balance)


if __name__ == '__main__':
    main()


# 3. 多线程的资源竞争与调度

"""
1. 多个线程竞争一个资源：保护临界资源 - 锁（Lock/RLock）
2. 多个线程竞争多个资源（线程数 > 资源数）- 信号量（Semaphore）
3. 多个线程的调度：暂停线程执行/唤醒等待中的线程 - Condition
"""

from concurrent.futures import ThreadPoolExecutor
from random import randint
from time import sleep

import threading

class Account:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.RLock()
        self.condition = threading.Condition(self.lock)

    def withdraw(self, money):
        """取钱"""
        with self.condition:
            while money > self.balance:    # 余额不足时等待
                # self.condition.wait()    # 释放锁并等待通知
                got_fund = self.condition.wait_for(lambda: self.balance >= money, timeout=10)
                if not got_fund:
                    raise TimeoutError("取款超时：余额不足")

            self.balance -= money
        
        # 把耗时模拟移到锁外
        sleep(0.001)

    def deposit(self, money):
        """存钱"""
        with self.condition:
            self.balance += money
            self.condition.notify_all()
        
        sleep(0.001)

def add_money_worker(account):
    for _ in range(6):
        money = randint(5, 10)
        with account.condition:
            account.deposit(money)
            print(threading.current_thread().name,
                ':', money, '======>', account.balance)

        sleep(0.5)

def sub_money_worker(account):
    for _ in range(3):
        money = randint(10, 30)
        with account.condition:
            account.withdraw(money)
            print(threading.current_thread().name,
                ':', money, '<======', account.balance)

        sleep(0.5)

def main():
    account = Account(10)
    with ThreadPoolExecutor(max_workers=15) as executor:
        for _ in range(10):    # 10 个线程存钱
            executor.submit(add_money_worker, account)

        for _ in range(5):    # 5 个线程取钱
            executor.submit(sub_money_worker,account)

if __name__ == '__main__':
    main()


# 4. 多进程

"""
多进程和进程池的使用
多线程因为 GIL(全局解释器锁) 的存在不能够充分发挥 CPU 的多核能力，尤其在计算密集型的任务中。

"""

import concurrent.futures
import math

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5

def is_prime(n):
    """判断素数"""

    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False

    return True

def main():
    """主函数"""
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


if __name__ == '__main__':
    main()

