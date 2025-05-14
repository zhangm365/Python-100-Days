"""
面向对象进阶
"""

# 1. 学生类
class Student:
    def __init__(self, name, age):
        self.__name = name    # __name 表示该属性是私有的
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}')

stu = Student('王大锤', 18)
stu.study('《Python 程序设计》')


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student('王大锤', 20)
stu.sex = '男'    # 动态为对象增加属性


# 2. 三角形类

class Triangle(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    @staticmethod
    def is_valid(a, b, c):
        """判断三条边是否构成三角形(静态方法)"""
        return a + b > c and a + c > b and b + c > a

    # 给方法增加一个 property 装饰器，将方法变成属性
    @property
    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    @property
    def area(self):
        """计算面积"""
        p = self.perimeter / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

t = Triangle(3,4, 5)
print(f'周长:{t.perimeter}')
print(f'面积:{t.area}')


# 3. 继承和多态

class Person:
    """人"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭.')

    def sleep(self):
        print(f'{self.name}正在睡觉.')

# 继承自 Person 类
class Student(Person):

    def __init__(self, name, age):
        super().__init__(name, age)    # 调用父类初始化方法

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师"""
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}正在讲授{course_name}.')

stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)

tea1 = Teacher('武则天', 34, '副教授')
stu1.eat()
stu1.study('《Python 程序设计》')
stu2.sleep()
stu2.study('《大模型原理与应用》')

tea1.teach('《机器人导论》')

