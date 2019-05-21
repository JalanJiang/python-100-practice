"""
判断输入的边长能否构成三角形
如果能则计算出三角形的周长和面积
海伦公式：area = sqrt(p(p-a)(p-b)(p-c))

Version: 1.0.0
Author: Jalan
"""
import math

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    p = a + b + c
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print("周长 = %.2f，面积 = %.2f" % (p, area))
else:
    print("无法构成三角形")