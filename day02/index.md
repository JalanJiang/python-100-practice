# Day02 - 语言元素

## 指令和程序

计算机硬件系统的五大部件：

- 运算器
- 控制器
- 存储器
- 输入设备
- 输出设备

运算器 + 控制器 = 中央处理器（CPU）

任务：复习冯·诺依曼结构。

## 变量和类型

1. 整型
    - 可以处理任意大小的整数（不存在溢出情况）
    - 支持二进制（如`0b100`，换算成十进制是4）、八进制（如`0o100`，换算成十进制是64）、十进制（`100`）和十六进制（`0x100`，换算成十进制是256）的表示法
2. 浮点型
3. 字符串型
4. 布尔型：`True` / `False`
5. 复数型
   
## 变量命名

PER 8 要求：

- 用小写字母拼写，多个单词用下划线连接
- 受保护的实例属性用单个下划线开头
- 私有的实例属性用两个下划线开头

## 变量强制转换

- `int()`：将一个数值或字符串转换成整数，可以指定进制
- `float()`：将一个字符串转换成浮点数
- `str()`：将指定的对象转换成字符串形式，可以指定编码
- `chr()`：将整数转换成该编码对应的字符串（一个字符）
- `ord()`：将字符串（一个字符）转换成对应的编码（整数）

----

## 练习

### 练习1：华氏温度转摄氏温度

```python
"""
练习1：华氏温度转摄氏温度
公式：F = 1.8C + 32

Version: 1.0
Author: Jalan
"""

f = float(input("请输入华氏温度："))
c = (f - 32) / 1.8
print("%.1f 华氏度 = %.1f 摄氏度" % (f, c))
```

运行结果如下：

```zsh
➜  python-100-practice git:(master) ✗ /usr/local/opt/python/bin/python3.7 /Users/jalan/www/own/python-100-practice/day02/code/practice.py
请输入华氏温度：100
100.0 华氏度 = 37.8 摄氏度
```

知识点：

- `input()` 接收终端参数
- `float()` 强制类型转换
- `print()`
  - 使用 `%.1f` 格式化数据为小数点后一位
  - `print("..." % (a, b))` 格式

### 练习2：输入圆的半径计算计算周长和面积

```python
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
```

运行结果如下：

```zsh
➜  python-100-practice git:(master) ✗ /usr/local/opt/python/bin/python3.7 /Users/jalan/www/own/python-100-practice/day02/code/practice2.py
请输入圆的半径：10
周长 = 62.8
面积 = 314.2
```

知识点：

- 圆周率：`math.pi`

### 练习3：输入年份判断是不是闰年

```python
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
```

运行结果：

```zsh
➜  python-100-practice git:(master) ✗ /usr/local/opt/python/bin/python3.7 /Users/jalan/www/own/python-100-practice/day02/code/practice3.py
请输入年份：2008
True
```
