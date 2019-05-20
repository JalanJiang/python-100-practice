"""
练习1：华氏温度转摄氏温度
公式：F = 1.8C + 32

Version: 1.0
Author: Jalan
"""

f = float(input("请输入华氏温度："))
c = (f - 32) / 1.8
print("%.1f 华氏度 = %.1f 摄氏度" % (f, c))