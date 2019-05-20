"""
练习2：输入圆的半径计算计算周长和面积
周长公式：2*pi*r
面积公式：pi*r*r

Version: 1.0.0
Author: Jalan
"""

import math

r = float(input("请输入圆的半径："))
perimeter = math.pi * 2 * r
area = math.pi * r * r

print("周长 = %.1f" % perimeter)
print("面积 = %.1f" % area)