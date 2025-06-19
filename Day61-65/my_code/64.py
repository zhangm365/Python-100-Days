
"""
使用 selenium 库模拟浏览器操作，获取网页内容
"""

# 1. 使用 selenium 库模拟浏览器操作

from selenium import webdriver

browser = webdriver.Chrome()  # 创建浏览器对象
browser.get('https://www.github.com/')  # 打开网页
print(browser.title)  # 打印网页标题
browser.quit()  # 关闭浏览器


# 2. 点击操作

from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


browser = webdriver.Chrome()
browser.set_window_size(1280, 800)  # 设置浏览器窗口大小

browser.get('https://www.baidu.com/')
browser.implicitly_wait(10)  # 隐式等待，最长等待10秒

kw_input = browser.find_element(By.ID, 'kw')  # 定位输入框
kw_input.send_keys('Python')  # 模拟用户输入关键词
search_button = browser.find_element(By.CSS_SELECTOR, '#su')  # 定位搜索按钮
search_button.click()  # 点击搜索按钮

wait_obj = WebDriverWait(browser, 10)
wait_obj.until(
    expected_conditions.presence_of_element_located(    # 定位的元素加载完成
        (By.CSS_SELECTOR, '#content_left')
    )
)

# 执行 JavaScript 代码: 将网页滚到最下方
browser.execute_script('document.documentElement.scrollTop = document.documentElement.scrollHeight')

browser.get_screenshot_as_file('baidu_search_result.png')  # 截图保存
browser.quit()  # 关闭浏览器

# 3. selenium 反爬的破解

from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 禁用自动化提示
options.add_experimental_option('useAutomationExtension', False)  # 禁用自动化扩展

browser = webdriver.Chrome(options=options)  # 创建浏览器对象

# 执行Chrome开发者协议命令（在加载页面时执行指定的JavaScript代码）
browser.execute_cdp_cmd(
    'Page.addScriptToEvaluateOnNewDocument',
    {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'}
)

browser.set_window_size(1280, 800)  # 设置浏览器窗口大小

browser.get('https://www.baidu.com/')
browser.implicitly_wait(10)  # 隐式等待，最长等待10秒

kw_input = browser.find_element(By.ID, 'kw')  # 定位输入框
kw_input.send_keys('Python')  # 模拟用户输入关键词
search_button = browser.find_element(By.CSS_SELECTOR, '#su')  # 定位搜索按钮
search_button.click()  # 点击搜索按钮

wait_obj = WebDriverWait(browser, 10)
wait_obj.until(
    expected_conditions.presence_of_element_located(    # 定位的元素加载完成
        (By.CSS_SELECTOR, '#content_left')
    )
)

# 执行 JavaScript 代码: 将网页滚到最下方
browser.execute_script('document.documentElement.scrollTop = document.documentElement.scrollHeight')

browser.get_screenshot_as_file('baidu_search_result.png')  # 截图保存
browser.quit()  # 关闭浏览器
