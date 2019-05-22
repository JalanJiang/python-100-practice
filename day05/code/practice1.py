"""
找出100~999之间的所有水仙花数
水仙花数是各位立方和等于这个数本身的数
如: 153 = 1**3 + 5**3 + 3**3

Version: 1.0.0
Author: Jalan
Date: 2019-05-22
"""

res = []
for num in range(100, 1000):
    tmp = num
    c = tmp % 10
    tmp //= 10
    b = tmp % 10
    tmp //= 10
    a = tmp % 10
    if num == a**3 + b**3 + c**3:
        # 转为 string 类型，否则 join 会报错
        res.append(str(num))
res_string = ", ".join(res)
print("水仙花数有：%s" % res_string)