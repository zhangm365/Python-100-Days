
"""
异步 I/O - async/await
Python3.7+ 通过 await 和 async 关键字实现异步 I/O

"""

import asyncio

def num_generator(m, n):
    """指定范围的数据生成器"""
    yield from range(m, n + 1)

async def prime_filter(m, n):
    """素数过滤器"""
    primes = []
    for i in num_generator(m, n):
        flag = True
        for j in range(2, int(i ** 0.5 + 1)):
            if i % j == 0:
                flag = False
                break
        
        if flag:
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)  # 模拟异步 I/O 操作

    return tuple(primes)

async def square_mapper(m, n):
    """平方映射器"""
    squares = []
    for i in num_generator(m, n):
        square = i * i
        print('Square =>', square)
        squares.append(square)

        await asyncio.sleep(0.001)  # 模拟异步 I/O 操作

    return tuple(squares)

async def main():
    """主函数：并发执行，拿到两个结果后统一处理"""
    primes, squares = await asyncio.gather(
        prime_filter(2, 100),
        square_mapper(1, 100),
    )
    print(f"\n共找到 {len(primes)} 个素数，示例：{primes[:5]} …")
    print(f"平方列表前 5 项：{squares[:5]} …")

if __name__ == '__main__':
    asyncio.run(main())


"""aiohttp 异步 HTTP 库"""
import asyncio
import re

import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')

async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()

async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        m = PATTERN.search(html)
        if m:
            print(m.group('title'))
        else:
            print(f"[WARN] 在 {url} 中未找到 <title> 标签")

async def fetch_all_titles():
    urls = (
        'https://www.python.org/',
        'https://git-scm.com/',
        'https://www.jd.com/',
        'https://www.taobao.com/',
        'https://www.douban.com/'
    )
    # 用 asyncio.gather 并发执行所有 show_title
    await asyncio.gather(*(show_title(url) for url in urls))

if __name__ == '__main__':
    asyncio.run(fetch_all_titles())
