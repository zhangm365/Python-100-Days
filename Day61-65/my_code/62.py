
"""
使用 requests 库访问网页内容
"""

import requests
# 使用 BeautifulSoup 解析 HTML 内容
from bs4 import BeautifulSoup

url = 'https://www.github.com/'
headers = {
    'User-Agent': 'Mozilla/5.0'
}

resp = requests.get(url, headers=headers)
print(resp.status_code)
if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            print(link['href'])
            # print(link.get('title', 'No title'))
            if 'title' in link.attrs:
                print(link['title'])

# 获取 google logo 图片并保存.
resp = requests.get('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')
with open('google.png', 'wb') as file:
    file.write(resp.content)