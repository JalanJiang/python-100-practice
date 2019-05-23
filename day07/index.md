# Day07 - 字符串和常用数据结构

## 字符串

### 切片

```Python
str2 = 'abc123456'
# 从字符串中取出指定位置的字符(下标运算)
print(str2[2])  # c
# 字符串切片(从指定的开始索引到指定的结束索引)
print(str2[2:5])  # c12
print(str2[2:])  # c123456
print(str2[2::2])  # c246
print(str2[::2])  # ac246
print(str2[::-1])  # 654321cba
print(str2[-3:-1])  # 45
```

- `[x:y]`：从下标 `x` 往后取到下标为 `y - 1`（半开区间）
- `[x:]`：从下标 `x` 开始取到末尾
- `[x::y]`：从下标 `x` 开始每间隔 `y` 取一个元素，取出的元素下标为 `x, x + y, x + 2y ......`
- `[::y]`：从首项开始每间隔 `y` 取一个元素，取出元素下标为 `0, y, 2y ......`
- `[-x:-y]`：从倒数第 3 个元素取到倒数第 2 个元素（-1 半开区间，所以取不到倒数第一个）

学习资料：[廖雪峰 Python 切片](https://www.liaoxuefeng.com/wiki/897692888725344/923029651584288)

## 列表

- 排序
    - `list = sorted(list)` 返回排序后的结果
    - `list.sort()` 直接在列表对象上排序

### 生成器

#### 列表生成式

[列表生成式](https://www.liaoxuefeng.com/wiki/897692888725344/923029657876192)

#### yield

通过 `yield` 关键字将一个普通函数改造成生成器函数。

```python
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
```

## 元组

- 元素**无法修改**
  - 一个不变的对象比一个可变的对象更加容易维护
  - 一个不变对象自动就是线程安全的，可以省去同步化的开销
  - 一个不变的对象方便被共享访问
- 在创建时间和占用空间上都优于列表

```python
# 定义元组
t = ('test', 'test1', 'test2')

# 列表转元组
t = tuple(l)
```

## 集合

- 不允许有重复元素
- 可以计算交集、并集、差集
  
```python
set1 = {1, 2, 3}
set2 = set(range(1, 10))

# 添加元素
set1.add(4)
set2.update([11, 12])

# 移除元素
set1.discard(1) # 如果元素不存在不会报错
set2.remove(11) # 如果元素不存在会报错

# 元组转集合
set3 = set((1, 2, 3, 4, 5))

# 集合的交集、并集、差集、对称差运算
print(set1 & set2) #交
# print(set1.intersection(set2))
print(set1 | set2) #并
# print(set1.union(set2))
print(set1 - set2) #差
# print(set1.difference(set2))
print(set1 ^ set2) #对称差
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))
```

## 字典

- 键值对

```python
scores = {"Tom": 100, "Jan": 88, "Som": 60}
# 更新与新增
scores.update(Maria=100, Jack=90)
# 获取
scores.get("Tom", 80)
# 删除
print(scores.popitem())
print(scores.pop("Tom", 20))
# 清空
scores.clear()
```

## 练习

### 练习1：在屏幕上显示跑马灯文字

```python
"""
在屏幕上显示跑马灯文字
打印一段文字，休眠，清理屏幕，打印……

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""
import os
import time

def main():
    content = "今天是个好日子啊……"
    while True:
        os.system('clear')
        print(content)

        # 休眠
        time.sleep(0.2)
        # 制造跑马灯效果
        content = content[1:] + content[0]
    
if __name__ == "__main__":
    main()
```

知识点：

- `time.sleep()` 休眠
- `os.system('clear')` 清屏
  
### 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成

```python
"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""
import random

def generate_code(code_length=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码长度（默认 4 个字符）

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    # 大写字母
    upper_list = [chr(x) for x in range(ord('A'), ord('A') + 26)]    
    #print(upper_list)
    # 小写字母
    lower_list = [chr(x) for x in range(ord('a'), ord('a') + 26)]
    #print(lower_list)
    # 0-9 数字
    digit_list = [x for x in range(0, 10)]
    #print(digit_list)
    res_list = upper_list + lower_list + digit_list
    res_list_len = len(res_list)
    code = ''
    for _ in range(code_length):
        index = random.randint(0, res_list_len - 1)
        code += res_list[index]
    return code

def main():
    code_len = int(input('请输入验证码长度：'))
    print(generate_code(code_len))

if __name__ == '__main__':
    main()
```

因为懒得手打字母表，所以用了列表生成式用于生成 26 个字母。

知识点：

- `ord()`：是 `chr()` 函数（对于8位的ASCII字符串）或 `unichr()` 函数（对于 Unicode 对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值
- `chr()`：用一个范围在 `range(256)` 内的（就是0～255）整数作参数，返回一个对应的字符

参考：

- [Python ord() 函数](https://www.runoob.com/python/python-func-ord.html)
- [Python chr() 函数](https://www.runoob.com/python/python-func-chr.html)
  
### 练习3：设计一个函数返回给定文件名的后缀名

```python
"""
设计一个函数返回给定文件名的后缀名

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""

def get_suffix(filename, has_dot=True):
    """
    获取文件名后缀

    :param filename: 文件名
    :param has_dot: 后缀是否需要带点
    :return: 文件名后缀
    """
    pos = filename.rfind('.')
    if pos != -1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''

def main():
    filename = str(input('输入文件名：'))
    print(get_suffix(filename, False))

if __name__ == '__main__':
    main()
```

知识点：

- [Python3 rfind()方法](https://www.runoob.com/python3/python3-string-rfind.html)，返回字符串最后一次出现的位置

### 练习4：设计一个函数返回传入的列表中最大和第二大的元素的值

```python
"""
练习4：设计一个函数返回传入的列表中最大和第二大的元素的值

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""

def get_top2_element(element_list):
    """
    返回传入列表最大和第二大元素的值

    :param element_list: 传入列表
    :return 最大和第二大元素
    """
    element_list.sort(reverse=True)
    return element_list[:2]

def main():
    element_list = [2, 5, 10, 22]
    print(get_top2_element(element_list))

if __name__ == '__main__':
    main()
```

偷懒，直接用了 `sort`。看了下骆昊老师的例子是用了交换的方法，循环遍历列表，然后找到比当前 m1 m2 大的数就进行替换。

### 练习5：计算指定的年月日是这一年的第几天

```
"""
练习5：计算指定的年月日是这一年的第几天

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""

def is_leap_year(year):
    """
    判断是否是闰年
    
    :param year: 年
    :return 闰年返回 True，非闰年返回 False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def which_day(year, month, day):
    """
    返回指定的年月日是这一年的第几天

    :param year: 年
    :param month: 月
    :param day: 日
    :return 第几天
    """
    month_day = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    # 闰年
    if is_leap_year:
        month_day[2] = 29

    day_count = 0
    for i in range(1, month):
        day_count += month_day[i]
    day_count += day

    return day_count


def main():
    print(which_day(2019, 5, 23))

if __name__ == '__main__':
    main()
```

### 练习6：打印杨辉三角

```python
"""
练习6：打印杨辉三角

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""

def main():
    row = int(input('输入行数：'))

    # 初始化列表
    yh_triangle = [[] for _ in range(row)]

    for i in range(row):
        if i == 0:
            yh_triangle[i] = [1]
        elif i == 1:
            yh_triangle[i] = [1, 1]
        else:
            yh_triangle[i].append(1)
            for j in range(1, len(yh_triangle[i - 1])):
                # 每个数等于它上方两数之和
                yh_triangle[i].append(yh_triangle[i - 1][j] + yh_triangle[i - 1][j - 1])
            yh_triangle[i].append(1)
        print(yh_triangle[i], end="\n")


if __name__ == '__main__':
    main()
```

## 综合案例

### 案例1：双色球选号

不想去了解双色球的规则了。。。这题先放空。。。

### 案例2：约瑟夫环问题

[约瑟夫问题](https://zh.wikipedia.org/wiki/%E7%BA%A6%E7%91%9F%E5%A4%AB%E6%96%AF%E9%97%AE%E9%A2%98)

用模拟整个过程的方式来做，被扔掉的人标记 `False`。

```python
"""
约瑟夫问题

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""

def main():
    # 初始化，还没被扔掉的标为 True
    persons = [True for _ in range(30)]
    count, index, number = 0, 0, 0
    while count < 15:
        if persons[index]:
            number += 1 # 计数
            if number == 9:
                # 被扔掉
                persons[index] = False
                # 扔掉的人数 + 1
                count += 1
                # 重新开始计数
                number = 0
        index += 1
        index %= 30
    
    for person in persons:
        print('是基督徒' if person else '不是基督徒')

if __name__ == "__main__":
    main()
```

### 案例3：井字棋游戏

[井字棋](https://zh.wikipedia.org/wiki/%E4%BA%95%E5%AD%97%E6%A3%8B)。

顺便自己补充了判赢逻辑。

```
"""
井字棋

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""

import os

def print_board(board):
    """
    画格子

    :param board: 每个格子的内容
    """
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def is_winner(board, turn):
    """
    判断走棋者是否是赢家

    :param board: 当前棋盘数据
    :param turn: 走棋者
    :return 走棋者是赢家返回 True，否则返回 False
    """
    return ((board['TL'] == turn and board['TM'] == turn and board['TR'] == turn) or
    (board['ML'] == turn and board['MM'] == turn and board['MR'] == turn) or
    (board['BL'] == turn and board['BM'] == turn and board['BR'] == turn) or
    (board['TL'] == turn and board['ML'] == turn and board['BL'] == turn) or
    (board['TM'] == turn and board['MM'] == turn and board['BM'] == turn) or
    (board['TR'] == turn and board['MR'] == turn and board['BR'] == turn) or
    (board['TL'] == turn and board['MM'] == turn and board['BR'] == turn) or
    (board['BL'] == turn and board['MM'] == turn and board['TR'] == turn))

def main():
    # 初始化一个空棋盘
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    # print_board(init_board)

    begin = True
    
    while begin:
        # 开始一盘新棋局
        current_board = init_board.copy()
        begin = False

        # 轮到 x 走
        turn = 'x'
        # 已经走了几个格子
        counter = 0

        # 清屏
        os.system('clear')

        print_board(current_board)

        while counter < 9:
            move = input('轮到 %s 走，请输入位置：' % turn)
            if current_board[move] == ' ':
                counter += 1
                current_board[move] = turn

                if is_winner(current_board, turn):
                    print("产生赢家：%s 赢得胜利" % turn)
                    break

                turn = 'o' if turn == 'x' else 'x'

            os.system('clear')
            print_board(current_board)

        choice = input('是否再玩一局？(y/n)')
        begin = choice == 'y'


if __name__ == "__main__":
    main()
```