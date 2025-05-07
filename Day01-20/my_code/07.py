"""
 1. 100 以内的素数
"""
from random import betavariate

print("100 以内的素数:")
for num in range(2, 101):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num)

"""
2. 斐波那契数列:
1, 1, 2, 3, 5, 8, 13, 21, 34 ...
"""
print("20 以内的斐波那契数列:")
a, b = 0, 1
for _ in range(20):
    a, b = b, a + b
    print(a)


"""
3. 水仙花数：100-999 之间的水仙花数
"""

print("100-999 之间的水仙花数:")
for num in range(100, 1000):
    a = num // 100
    b = num // 10 % 10
    c = num % 10
    if a ** 3 + b ** 3 + c ** 3 == num:
        print(num)


"""
4. 百钱百鸡：100 块买 100 只鸡
"""
print("百钱百鸡：")
for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(f'公鸡：{x} 只，母鸡：{y} 只，小鸡：{z} 只')

"""
骰子游戏
"""
import random

money = 1000
while money > 0:
    print(f'您的总资产为: {money} 元')
    while True:
        debt = int(input("请下注："))
        if 0 < debt <= money:
            break
    first_point = random.randrange(1, 7) + random.randrange(1, 7)

    print(f'\n第一次掷骰子结果为: {first_point} 点')
    if first_point == 7 or first_point == 11:
        money += debt
        print("玩家胜！")
    elif first_point == 2 or first_point == 3 or first_point == 12:
        money -= debt
        print("庄家胜！")
    else:
        while True:
            sec_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'\n玩家掷骰子结果为: {sec_point} 点')
            if sec_point == 7:
                money -= debt
                print("庄家胜！")
                break
            elif sec_point == first_point:
                money += debt
                print("玩家胜！")
                break

print("您的资产为 0，游戏结束！")

