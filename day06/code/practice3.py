"""
实现判断一个数是不是素数的函数

Version: 1.0.0
Author: Jalan
Date: 2019-05-22
"""
from math import sqrt

def is_prime(num):
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
    return True if num != 1 else False

n = int(input("输入 n："))
print(is_prime(n))