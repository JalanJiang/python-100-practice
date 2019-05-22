"""
求解《百钱百鸡》问题
1 只公鸡 5 元 1 只母鸡 3 元 3 只小鸡 1 元 用 100 元买 100 只鸡
问公鸡 母鸡 小鸡各有多少只

Version: 1.0.0
Author: Jalan
Date: 2019-05-22
"""

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z /3 == 100:
            print("公鸡 %d, 母鸡 %d, 小鸡 %d" % (x, y, z))