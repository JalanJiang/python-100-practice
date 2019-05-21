# Day03 - 分支结构

- Python 中使用 `elif` 而非像别的语言那样是 `elseif`
- **Flat is better than nested**：尽量减少嵌套次数

## 练习

### 练习1：英制单位与公制单位互换

```python
"""
英制单位英寸和公制单位厘米互换
1英寸(in) = 2.54厘米(cm)

输入：长度 value 与 单位 unit
输出：另外一类的长度与单位

Version: 1.0.0
Author: Jalan
"""

value = float(input("请输入长度："))
unit = input("请输入单位：")

# 如果输入的是厘米
if unit == "cm" or unit == "厘米":
    output_value = value / 2.54
    print("%f 厘米 = %f 英寸" % (value, output_value))
# 如果输入的是英寸
elif unit == "in" or unit == "英寸":
    output_value = value * 2.54
    print("%f 英寸 = %f 厘米" % (value, output_value))
# 输入的单位无效
else:
    print("请输入有效单位")
```

注意点：判断输入的单位有效性

### 练习2：掷骰子决定做什么

```
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
```

知识点：使用 `random` 模块的 `randint` 函数生成特定范围的随机数。

`random` 常见函数如下：

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

print( random.randint(1,10) )        # 产生 1 到 10 的一个整数型随机数  
print( random.random() )             # 产生 0 到 1 之间的随机浮点数
print( random.uniform(1.1,5.4) )     # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
print( random.choice('tomorrow') )   # 从序列中随机选取一个元素
print( random.randrange(1,100,2) )   # 生成从1到100的间隔为2的随机整数

a=[1,3,5,6,7]                # 将序列a中的元素顺序打乱
random.shuffle(a)
print(a)
```

这道题如果不属于分支结构分类的话，我可能会用字典来写：

```python
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
```

### 练习3：百分制成绩转等级制

```python
"""
百分制成绩转等级制成绩
90分以上    --> A
80分~89分    --> B
70分~79分	   --> C
60分~69分    --> D
60分以下    --> E

Version: 1.0.0
Author: Jalan
"""

score = float(input("请输入成绩："))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "E"

print("成绩等级是：%s" % grade)
```

### 练习4：输入三条边长如果能构成三角形就计算周长和面积

```python
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
```

完全忘记三角形面积怎么算了……😓然后复习了海伦公式……

### 练习5：个人所得税计算器

```python
"""
输入月收入和五险一金计算个人所得税

Version 1.0.0
Author: Jalan
"""

salary = float(input("本月收入："))
insurance = float(input("五险一金："))
diff = salary - insurance - 5000

if diff <= 0:
    rate = 0
    deduction = 0
elif diff < 3000:
    rate = 0.03
    deduction = 0
elif diff < 12000:
    rate = 0.1
    deduction = 210
elif diff < 25000:
    rate = 0.2
    deduction = 1410
elif diff < 35000:
    rate = 0.25
    deduction = 2660
elif diff < 55000:
    rate = 0.3
    deduction = 4410
elif diff < 80000:
    rate = 0.35
    deduction = 7160
else:
    rate = 0.45
    deduction = 15160

tax = abs(diff * rate - deduction)
print('个人所得税: ￥%.2f元' % tax)
print('实际到手收入: ￥%.2f元' % (diff + 5000 - tax))
```

个税表可以参考：[2018年新版个税计算器（5000起征点）](http://www.chineseacc.com/tool/gsjsq/2018-07-31/2923.html)

知识点：`abs()` 用于处理 `-0` 的问题