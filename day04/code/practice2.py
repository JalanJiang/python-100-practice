"""
输入两个正整数计算最大公约数和最小公倍数

Version: 1.0.0
Author: Jalan
Date: 2019-05-21
"""

x = int(input("x = "))
y = int(input("y = "))

if x > y:
    x, y = y, x

for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("%d 和 %d 的最大公约数为 %d" % (x, y, factor))
        print("%d 和 %d 的最小公倍为 %d" % (x, y, x * y // factor))
        break