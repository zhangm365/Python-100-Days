
"""
1. 使用 requests 库访问网页内容
2. 使用 BeautifulSoup 解析 HTML 内容
"""

import requests
# BeautifulSoup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup

url = 'https://www.github.com/'
# 设置请求头，模拟浏览器访问
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
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
    file.write(resp.content)    # resp.content 返回的是二进制内容


# 获取豆瓣电影 Top 250 页面
print("\n===== 豆瓣电影 Top 250: =====")
for page in range(1, 11):
    url = f'https://movie.douban.com/top250?start={(page - 1) * 25}'
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        for item in soup.find_all('div', class_='item'):
            rank  = item.find('em').text
            title = item.find('span', class_='title').text
            print(rank, title)
    else:
        print(f'Failed to retrieve page {page}')

