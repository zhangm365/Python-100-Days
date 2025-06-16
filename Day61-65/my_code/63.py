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


# 2. 继承 Thread 类创建线程对象

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
