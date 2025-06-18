
"""
异步编程
"""


# 1. yield 关键字：该函数会得到一个生成器对象

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

import asyncio    # 提供异步 I/O 的支持模块
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


# 3. 异步 I/O 执行爬虫程序

import asyncio
import aiohttp
import re

from aiohttp import ClientSession

TITLE_PATTERN = re.compile(r'<title.*?>(.*?)</title>', re.IGNORECASE)

async def fetch_page_title(url):
    async with aiohttp.ClientSession(headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    }) as session:
        async with session.get(url, ssl=False) as resp:
            if resp.status != 200:
                return f'Error: {resp.status}'
            content = await resp.text()
            match = TITLE_PATTERN.search(content)
            title = match.group(1).strip() if match else 'No title found'
            print(f'URL: {url}, Title: {title}')

async def main():
    urls = [
        'https://www.baidu.com',
        'https://git-scm.com/',
        'https://www.jd.com',
        'https://www.amazon.com/',
        'https://www.taobao.com'
    ]
    start = time.time()
    tasks = [fetch_page_title(url) for url in urls]
    await asyncio.gather(*tasks)
    end = time.time()
    print(f'耗时: {end - start:.3f} 秒.')

if __name__ == '__main__':
    asyncio.run(main())


print('--------requests: ---------')
import requests
import time
import re
TITLE_PATTERN = re.compile(r'<title.*?>(.*?)</title>', re.IGNORECASE)

def fetch_page_title(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
    }
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return f'Error: {resp.status_code}'
    content = resp.text    # string type
    match = TITLE_PATTERN.search(content)
    title = match.group(1).strip() if match else 'No title found'
    print(f'URL: {url}, Title: {title}')

def main():
    urls = [
        'https://www.baidu.com',
        'https://git-scm.com/',
        'https://www.jd.com',
        'https://www.amazon.com/',
        'https://www.taobao.com'
    ]
    start = time.time()
    for url in urls:
        fetch_page_title(url)
    end = time.time()
    print(f'耗时: {end - start:.3f} 秒.')


if __name__ == '__main__':
     main()
