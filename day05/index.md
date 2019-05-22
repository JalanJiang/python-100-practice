# Day05 - 练习

## 1. 寻找水仙花数

```python
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
```

## 2. 寻找完美数

[LeetCode 507. 完美数](https://leetcode-cn.com/problems/perfect-number/)

```python
"""
完美数是除自身外其他所有因子的和正好等于这个数本身的数
来自 LeetCode: 507. 完美数

Version: 1.0.0
Author: Jalan
Date: 2019-05-22
"""

import math

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num <= 1:
            return False
        
        s = 0
        for factor in range(1, int(math.sqrt(num)) + 1):
            # 判断是否是因子
            if num % factor == 0:
                s += factor
                # 避免相同因子重复添加
                if factor != 1 and num / factor != factor:
                    s += num / factor
            
        if s == num:
            return True
        else:
            return False
```

## 3. 百钱百🐔

模拟就对了。

```python
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
```

## 4. 生成斐波拉切数列

```python
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

```

## 5. Craps赌博游戏

```python
"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 1.0.0
Author: Jalan
Date: 2019-05-22
"""
import random

def get_random_num():
    num = random.randint(1, 6) + random.randint(1, 6)
    print("摇骰子点数为 %d" % num)
    return num

money = 1000
count = 1

while money > 0:
    print("第 %d 局开始，您的赌注为 %d 元" % (count, money))

    while True:
        debt = int(input('请下注: '))
        if debt > 0 and debt <= money:
            break

    first_num = get_random_num()
    if first_num == 7 or first_num == 11:
        money += debt
        print("本轮结束，玩家胜")
    elif first_num == 2 or first_num == 3 or first_num == 12:
        money -= debt
        print("本轮结束，庄家胜")
    else:
        second_num = get_random_num()
        if second_num == 7:
            money -= debt
            print("本轮结束，庄家胜")
        elif second_num == first_num:
            money += debt
            print("本轮结束，玩家胜")
        else:
            print("本轮结束，未分出胜负")
        
    count += 1

print("游戏结束，您身无分文")
```

写完发现还挺好玩的……