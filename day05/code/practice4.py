"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 1.0.0
Author: Jalan
Date: 2019-05-22
"""

a = 1
b = 1
for i in range(20):
    print("%d " % a, end="")
    a , b = b, a + b
