
"""
多进程
"""

# 1. 创建进程
# from multiprocessing import Process, current_process
# from time import sleep

# def sub_task(content, nums):
#     # 通过 current_process() 获取当前进程对象
#     # 获取进程对象的 pid 和 name 属性.
#     print(f'PID: {current_process().pid}')
#     print(f'Name: {current_process().name}')

#     counter, total = 0, nums.pop(0) if nums else 0
#     print(f'Loop count: {total}')
#     sleep(0.5)
#     while counter < total:
#         counter += 1
#         print(f'{content} {counter}')
#         sleep(0.01)

# def main():
#     nums = [10, 20, 30]
#     Process(target=sub_task, args=('Ping', nums)).start()
#     Process(target=sub_task, args=('Pong', nums)).start()
    
#     sub_task('Main', nums)

# if __name__ == '__main__':
#     main()


"""
多进程与多线程
"""

# 2. 多线程/多进程判断是否为素数

"""
比较多线程和多进程执行计算密集型任务的性能差距。
"""

import concurrent.futures

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095291,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5

def is_prime(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False
    return True

def main():
    # with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:    # 线程池
    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:    # 进程池
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print(f'{number} is prime: {prime}')

if __name__ == '__main__':
    main()


# 3. 多进程间的通信: 使用 Queue 实现进程间通信。

from multiprocessing import Process, Queue
import time

def sub_task(content, queue):
    counter = queue.get()    # 队列为空时默认阻塞
    while counter < 50:
        print(content, end='', flush=True)
        counter += 1
        queue.put(counter)
        time.sleep(0.01)
        counter = queue.get()

def main():
    queue = Queue()
    queue.put(0)  # 初始化计数器

    processes = [
        Process(target=sub_task, args=('Ping ', queue)),
        Process(target=sub_task, args=('Pong ', queue))
    ]

    for process in processes:
        process.start()

    # 等待进程中的某个结束
    while all(process.is_alive() for process in processes):
        pass
    
    # 主进程放置一个 >= 50 的计数器值，结束子进程
    queue.put(50)

if __name__ == '__main__':
    main()

