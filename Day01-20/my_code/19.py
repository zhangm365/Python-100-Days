"""
面向对象进阶
"""
class Student:
    def __init__(self, name, age):
        self.__name = name    # __name 表示该属性是私有的
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}')

stu = Student('王大锤', 18)
stu.study(' Python 程序设计')

