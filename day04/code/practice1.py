"""
输入一个正整数判断它是不是素数
素数：只能被 1 和它本身整除的数（1 不是素数）

Version: 1.0.0
Author: Jalan
Date: 2019-05-21
"""

import math

num = int(input("请输入一个整数："))
end = int(math.sqrt(num))

is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print("%d 是素数" % num)
else:
    print("%d 不是素数" % num)