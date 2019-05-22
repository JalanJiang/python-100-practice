# Day06 - 函数和模块的使用

## 定义函数

- `def` 关键字声明（和别的语言不太一样，PHP 是 `function`，Go 是 `func`）
- 函数名也采用小写字母 + 下划线方式：`xxx_yyy`
- `return` 关键字返回值
  
## 函数的参数

- 有默认值
- 支持可变参数（`*args`）
- 传参可指定顺序

因此 Python 不支持 [函数重载](https://zh.wikipedia.org/wiki/%E5%87%BD%E6%95%B0%E9%87%8D%E8%BD%BD)。

[为什么 Python 不支持函数重载？其他函数大部分都支持的？](https://www.zhihu.com/question/20053359)

## 用模块管理函数

- 模块用于解决命名冲突问题（类似 PHP 中的命名空间）
- 每个文件就是代表一个模块（module）

几种写法：

```python
from module1 import foo

foo()
```

```python
import module1 as m1

m1.foo()
```

```python
import modeul1 import foo

foo()
```

如果导入的模块除了定义函数之外还中有可以执行代码，那么 Python 解释器在导入这个模块时就会执行这些代码。

处理方式：将其余代码放入 `if __name__ == "__main__"` 条件中，只有直接执行的模块名字才叫做 `__main__`。

```python
def foo():
    pass


def bar():
    pass


# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()
```

### 变量作用域

- 没有定义在任何函数中的变量是全局变量（global variable）
- 定义在函数中的变量是局部变量（local variable）
- 变量查找顺序
  1. 局部作用域
  2. 嵌套作用域
  3. 全局作用域
  4. 内置作用域（内置的 `len` / `min` 等隐含标识）

如果要在函数内部修改全局变量，需要使用 `global` 关键字来指示变量来自于全局作用域：

```python
def foo():
    global a
    a = 200
    print(a)  # 200


if __name__ == '__main__':
    a = 100
    foo()
    print(a)  # 200
```

同理，使用 `nonlocal` 关键字可以指示嵌套作用域。

## 练习

### 练习1：实现计算求最大公约数和最小公倍数的函数

```python
"""
实现计算求最大公约数和最小公倍数的函数

Version: 1.0.0
Authro: Jalan
Date: 2019-05-22
"""
# 求最大公约数
def gcd(x, y):
    if x > y:
        x, y = y, x
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor

# 求最小公倍数
def lcm(x, y):
    return x * y // gcd(x, y)
```

### 练习2：实现判断一个数是不是回文数的函数

#### 解法一

用了双指针来做。

```python
"""
判断一个数是不是回文数的函数

Version: 1.0.0
Author: Jalan
Date: 2019-05-22
"""

def is_palindrome(num):
    num_string = str(num)
    i = 0
    j = len(num_string) - 1

    while i <= j:
        left = num_string[i]
        right = num_string[j]
        if left != right:
            return False
        i += 1
        j -= 1
        
    return True

n = int(input("输入数字："))
print(is_palindrome(n))
```

#### 解法二

求 `num` 反序数字再比较。

```python
"""
判断一个数是不是回文数的函数

Version: 2.0.0
Author: Jalan
Date: 2019-05-22
"""

def is_palindrome(num):
    temp  = num
    total = 0

    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    # 甚至想写一个条件结构，感觉有的时候自己写代码还是太啰嗦了……
    return total == temp

n = int(input("输入数字："))
print(is_palindrome(n))
```

### 练习3：实现判断一个数是不是素数的函数

```python
"""
实现判断一个数是不是素数的函数

Version: 1.0.0
Author: Jalan
Date: 2019-05-22
"""
from math import sqrt

def is_prime(num):
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
    return True if num != 1 else False
```

知识点：`return True if num != 1 else False` 简洁写法

### 练习4：写一个程序判断输入的正整数是不是回文素数

利用上面练习写好的函数就好了。

```python
if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)
```