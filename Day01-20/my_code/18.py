"""
面向对象编程
"""

# 1. 学生类
class Student:
    """学生类"""
    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        print(f'{self.name}正在玩游戏.')

stu1 = Student('张三', 18)
stu2 = Student('王大锤', 19)

stu1.study(' Python 程序设计')
stu2.play()


# 2. 时钟

import time
## 定义时钟类
class Clock:

    def __init__(self, hour = 0, minute = 0, second = 0):
        """初始化方法
        :param hour:小时
        :param minute:分钟
        :param second:秒
        """
        self.hour = hour
        self.min = minute
        self.sec = second

    def run(self):
        self.sec += 1
        if self.sec == 60:
            self.sec = 0
            self.min += 1
            if self.min == 60:
                self.min = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0

    def show(self):
        """显示时间"""
        return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'

clock = Clock(23, 59, 58)
print(clock.show())

time.sleep(1)
clock.run()

# 平面上的点
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def distance(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y

        return (dx * dx + dy * dy) ** 0.5

    def __str__(self):
        return f'({self.x}, {self.y})'

p1 = Point(1, 3)
p2 = Point(2, 5)
print(p1)
print(p2)

print(p1.distance(p2))