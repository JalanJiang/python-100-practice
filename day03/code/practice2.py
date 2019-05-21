"""
掷骰子决定做什么事情
摇出 1~6 的数字，判断要做什么事

Version: 1.0.0
Author: Jalan
"""

from random import randint

# 产生 1-6 的随机数
num = randint(1, 6)

if num == 1:
    res = "吃饭"
elif num == 2:
    res = "睡觉"
elif num == 3:
    res = "喵喵叫"
elif num == 4:
    res = "汪汪叫"
elif num == 5:
    res = "打豆豆"
elif num == 6:
    res = "写代码"

print(res)