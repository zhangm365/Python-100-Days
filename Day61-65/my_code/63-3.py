
"""
异步编程
"""


# 1.  yield 关键字：该函数会得到一个生成器对象

def fib(n):
    """计算斐波那契数列的第 n 项"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a

gen_obj = fib(10)
print(gen_obj)    # <generator object fib at 0x000001D0E050FCA0>

# for-in 遍历生成器中的值 
for value in gen_obj:
    print(value)


def calc_average():
    total, counter = 0, 0
    avg_value = None
    while True:
        cur_val = yield avg_value
        total += cur_val
        counter += 1
        avg_value = total / counter if counter else 0

def main():
    obj = calc_average()
    # 生成器预激活
    obj.send(None)
    for _ in range(5):
        print(f'当前平均值: {obj.send(float(input()))}')

if __name__ == '__main__':
    main()


# 2. 异步函数：async, await

import asyncio
import time

async def display(num):
    await asyncio.sleep(1)
    print(num)

async def main():
    start = time.time()
    await asyncio.gather(*(display(i) for i in range(1, 10)))
    end = time.time()
    print(f'耗时: {end - start:.3f} 秒.')

if __name__ == '__main__':
    asyncio.run(main())
