"""
判断一个数是不是回文数的函数

Version: 2.0.0
Author: Jalan
Date: 2019-05-22
"""

def is_palindrome(num):
    temp  = num
    total = 0

    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == temp

n = int(input("输入数字："))
print(is_palindrome(n))