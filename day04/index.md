# Day04 - 循环结构

- `for-in`：明确的知道循环执行的次数或者是要对一个容器进行迭代
- `while`：不知道具体循环次
- [range() 函数用法](https://www.runoob.com/python/python-func-range.html)

## 练习

### 练习1：输入一个数判断是不是素数

```python
"""
输入一个正整数判断它是不是素数
素数：只能被 1 和它本身整除的数（1 不是素数）

Version: 1.0.0
Author: Jalan
Date: 2019-05-21
"""

import math

num = int(input("请输入一个整数："))
end = int(math.sqrt(num))

is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num != 1:
    print("%d 是素数" % num)
else:
    print("%d 不是素数" % num)
```

### 练习2：输入两个正整数，计算最大公约数和最小公倍数

```python
"""
输入两个正整数计算最大公约数和最小公倍数

Version: 1.0.0
Author: Jalan
Date: 2019-05-21
"""

x = int(input("x = "))
y = int(input("y = "))

if x > y:
    x, y = y, x

for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print("%d 和 %d 的最大公约数为 %d" % (x, y, factor))
        print("%d 和 %d 的最小公倍为 %d" % (x, y, x * y // factor))
        break
```

知识点：

- 最大公约数和最小公倍数的求法（？？？😓）
- 学习了新的方法 `range(x, 0, -1)`，之前如果要反序的话我一般会用 `reversed(range(0, x + 1))`

### 练习3：打印三角形图案

```python
"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: Jalan
Date: 2019-05-21
"""

row = int(input("请输入行数："))

# 第一种三角形：第 x 行打印出 x 个星号
for i in range(row):
    for _ in range(i + 1):
        print("*", end="")
    print()

# 第二种三角形：第 x 行打印 row - x 个空格和 x 个星号
for i in range(row):
    row_num = i + 1
    space = row - row_num

    for _ in range(space):
        print(" ", end="")
    
    for _ in range(row_num):
        print("*", end="")
    
    print()

# 第三种三角形：每一行的星号数量是 1, 3, 5, 7, 9......

# 最后一行星号数量
max_num = 2 * row - 1

for i in range(row):
    row_num = i + 1
    # 当前行星号数量
    star_num = row_num * 2 - 1
    # 当前行左右分别存在空格数量
    space = int((max_num - star_num) / 2)

    for _ in range(space):
        print(" ", end="")
    
    for _ in range(star_num):
        print("*", end="")
    
    for _ in range(space):
        print(" ", end="")

    print()
```

```
    *
   ***
  *****
 *******
*********
```

打印第三种三角形👆的时候，我分了前、中、后三段进行打印。后面看了骆昊老师的代码：

```python
for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()
```

第三段的空格根本不用打嘛，傻了傻了🤦‍♂……
