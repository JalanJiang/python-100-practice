"""
实现计算求最大公约数和最小公倍数的函数

Version: 1.0.0
Authro: Jalan
Date: 2019-05-22
"""
# 求最大公约数
def gcd(x, y):
    if x > y:
        x, y = y, x
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

# 求最小公倍数
def lcm(x, y):
    return x * y // gcd(x, y)