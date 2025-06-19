
"""
并发编程在爬虫中的应用
"""


# 1. 单线程
"""
import requests
import os

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/137.0.0.0 Safari/537.36'
}

# 在源码同级目录下创建 images/beauty
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'images', 'beauty')

def download_image(url):
    print(url)
    resp = requests.get(url, headers=HEADERS)
    filename = url[url.rfind('/') + 1:]
    print(f'Downloading {filename}...')

    if resp.status_code == 200:
        with open(os.path.join(IMAGE_DIR, filename), 'wb') as f:
            f.write(resp.content)

def main():
    print('=========单线程爬虫程序开始下载图片...=========')
    url = 'https://image.so.com/zjl?ch=car'
    os.makedirs(IMAGE_DIR, exist_ok=True)

    # for i in range(3):
    resp = requests.get(f'{url}&sn=0', headers=HEADERS)

    if resp.status_code == 200:
        data = resp.json()    # JSON 解析，返回 dict
        for item in data.get('list', []):
            download_image(item['qhimg_url'])

if __name__ == '__main__':
    main()
"""

# 2. 多线程版本
"""
import requests
import os
from concurrent.futures import ThreadPoolExecutor
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/137.0.0.0 Safari/537.36'
}

# 在源码同级目录下创建 images/beauty
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'images', 'beauty')

def download_image(url):
    # print(url)
    resp = requests.get(url, headers=HEADERS)
    filename = url[url.rfind('/') + 1:]
    print(f'Downloading {filename}...')

    if resp.status_code == 200:
        with open(os.path.join(IMAGE_DIR, filename), 'wb') as f:
            f.write(resp.content)

def main():
    print('=========多线程爬虫程序开始下载图片...=========')
    url = 'https://image.so.com/zjl?ch=car'
    os.makedirs(IMAGE_DIR, exist_ok=True)

    start = time.time()
    with ThreadPoolExecutor(max_workers=8) as executor:
        resp = requests.get(f'{url}&sn=0', headers=HEADERS)
        # print(resp.status_code)
        if resp.status_code == 200:
            data = resp.json()    # JSON 解析，返回 dict
            futures = [executor.submit(download_image, item['qhimg_url']) for item in data.get('list', [])]
            for future in futures:
                future.result()  # 等待所有任务完成
    end = time.time()
    print(f'耗时: {end - start:.3f} 秒.')

if __name__ == '__main__':
    main()
"""

# 3. 异步版本

import asyncio
import aiohttp
import json
import os
import aiofile
import time

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/137.0.0.0 Safari/537.36'
}

# 在源码同级目录下创建 images/beauty
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'images', 'beauty')

async def download_image(session, url):
    # print(url)
    async with session.get(url, ssl=False) as resp:
        filename = url[url.rfind('/') + 1:]
        print(f'Downloading {filename}...')

        if resp.status == 200:
            data = await resp.read()  # 异步读取响应内容
            async with aiofile.async_open(os.path.join(IMAGE_DIR, filename), 'wb') as f:
                await f.write(data)

async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url = f'{url}&sn=0', 
            headers = HEADERS, 
            ssl = False
        ) as resp:
            if resp.status == 200:
                json_str = await resp.text()
                result = json.loads(json_str)  # JSON 解析，返回 dict
                for item in result.get('list', []):
                    await download_image(session, item['qhimg_url'])

async def main():
    print('=========异步爬虫程序开始下载图片...=========')
    url = 'https://image.so.com/zjl?ch=car'
    os.makedirs(IMAGE_DIR, exist_ok=True)

    start = time.time()
    await fetch_json(url)
    end = time.time()

    print(f'耗时: {end - start:.3f} 秒.')

if __name__ == '__main__':
    asyncio.run(main())

