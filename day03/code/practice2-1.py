"""
掷骰子决定做什么事情
摇出 1~6 的数字，判断要做什么事

Version: 1.0.0
Author: Jalan
"""

from random import randint

d = {1: "吃饭", 2: "睡觉", 3: "喵喵叫", 4: "汪汪叫", 5: "打豆豆", 6: "写代码"}
# 产生 1-6 的随机数
num = randint(1, 6)

print(d[num])