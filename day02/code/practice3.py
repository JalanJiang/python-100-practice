"""
输入年份 如果是闰年输出 True 否则输出 False
判断是否为闰年：
1. 普通闰年：能被4整除但不能被100整除的年份为普通闰年
2. 世纪闰年：能被400整除的为世纪闰年

Version: 1.0.0
Author: Jalan
"""

year = int(input("请输入年份："))

is_leap = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

print(is_leap)