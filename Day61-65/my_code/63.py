"""
多线程编程：threading 模块中的 Thread 类
"""

# 1. 文件下载：并发

from threading import Thread 
import time
import random

def download(*, filename):
    start = time.time()
    print(f"开始下载 {filename}...")
    time.sleep(random.randint(3, 6))  # 模拟下载时间
    end = time.time()
    print(f"{filename} 下载完成，耗时 {end - start:.3f} 秒.")

def main():
    print("============= 多线程并发下载文件：=============")
    files = ['file1.txt', 'file2.pdf', 'file3.mp4']
    threads = [Thread(target=download, kwargs={'filename': file}) for file in files]
        
    start = time.time()
    for thread in threads:
        thread.start()  # 启动线程

    for thread in threads:
        thread.join()  # 等待所有线程完成
    end = time.time()
    print(f"所有文件下载完成，总耗时 {end - start:.3f} 秒.")

if __name__ == '__main__':
    main()


# 2. 继承 Thread 类创建自定义线程对象

from threading import Thread
import time
import random

class DownloadThread(Thread):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
    
    def run(self):
        """重写 run 方法，定义线程执行的任务"""
        start = time.time()
        print(f"开始下载 {self.filename}...")
        time.sleep(random.randint(3, 6))  # 模拟下载时间
        end = time.time()
        print(f"{self.filename} 下载完成，耗时 {end - start:.3f} 秒.")

def main():
    print("============= 继承 Thread 类创建自定义线程对象：=============")
    files = ['file1.txt', 'file2.pdf', 'file3.mp4']
    threads = [DownloadThread(file) for file in files]

    start = time.perf_counter()    # 使用 perf_counter() 计时更精确
    for thread in threads:
        thread.start()  # 启动线程

    for thread in threads:
        thread.join()  # 等待所有线程完成
    end = time.perf_counter()

    print(f"所有文件下载完成，总耗时 {end - start:.3f} 秒.")

if __name__ == '__main__':
    main()


# 3. 线程池
"""
通过线程池的方式将任务放到多个线程中执行，通过线程池使用线程是多线程编程的较好方式。
因为，线程的创建和释放会带来较大的开销，线程池可以复用线程，减少开销。
"""

from concurrent.futures import ThreadPoolExecutor    # 线程池
import time
import random
from threading import Thread

def download(*, filename):
    start = time.time()
    print(f"开始下载 {filename}...")
    time.sleep(random.randint(3, 6))  # 模拟下载时间
    end = time.time()
    print(f"{filename} 下载完成，耗时 {end - start:.3f} 秒.")

def main():
    print("============= 线程池下载文件：=============")
    files = ['file1.txt', 'file2.pdf', 'file3.mp4']
    
    # 使用 ThreadPoolExecutor 创建线程池
    with ThreadPoolExecutor(max_workers=4) as executor:
        start = time.perf_counter()
        futures = [executor.submit(download, filename=file) for file in files]
        
        for future in futures:
            future.result()
        end = time.perf_counter()
    print(f"所有文件下载完成，总耗时 {end - start:.3f} 秒.")

if __name__ == '__main__':
    main()  


# 4. 守护线程

from threading import Thread
import time

def display(content):
    while True:
        print(content, end='', flush=True)
        time.sleep(0.1)

def main():
    Thread(target=display, args=('Ping ',), daemon=True).start()
    Thread(target=display, args=('Pong ',), daemon=True).start()
    time.sleep(3)

if __name__ == '__main__':
    main()


# 5. 资源竞争

from concurrent.futures import ThreadPoolExecutor
import time

class Account(object):
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """存款"""
        new_balance = self.balance + amount
        time.sleep(0.01)  # 模拟存款操作的延迟
        self.balance = new_balance

def main():
    account = Account()

    with ThreadPoolExecutor(max_workers=16) as executor:
        for _ in range(100):
            executor.submit(account.deposit, 1.0)

    print(f"账户余额: {account.balance}")

if __name__ == '__main__':
    main()


## 5.1 锁机制: RLock 保护共享资源。

from threading import RLock
from concurrent.futures import ThreadPoolExecutor
import time
from threading import Condition
import random

class Account(object):
    def __init__(self):
        self.balance = 0.0
        self.lock = RLock()
        self.condition = Condition(self.lock)  # 条件变量，用于线程间的通知


    def deposit(self, amount):
        """存款"""
        with self.condition:    # 使用锁来保护共享资源
            new_balance = self.balance + amount
            time.sleep(0.01)  # 模拟存款操作的延迟
            self.balance = new_balance
            self.condition.notify_all()  # 通知其他等待的线程余额已更新
    
    def withdraw(self, amount):
        """取款"""
        with self.condition:    # 使用锁来保护共享资源
            while amount > self.balance:
                print("余额不足，等待存款...")
                got_fund = self.condition.wait_for(lambda: self.balance >= amount, timeout=10)
                if not got_fund:
                    raise TimeoutError("取款超时：余额不足")
                        
            new_balance = self.balance - amount
            time.sleep(0.01)
            self.balance = new_balance

def main():
    account = Account()

    with ThreadPoolExecutor(max_workers=16) as executor:
        for _ in range(50):
            money = random.randint(5, 50)
            executor.submit(account.deposit, money)
        
        for _ in range(50):
            money = random.randint(1, 20)
            executor.submit(account.withdraw, money)

    print(f"账户余额: {account.balance}")

if __name__ == '__main__':
    main()