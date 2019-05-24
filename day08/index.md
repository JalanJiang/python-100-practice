# Day 08 - 面向对象编程基础

> We are all consenting adults here.

- 双下划线的变量或方法表示私有
  - 但仍然可以被访问
- 单下划线的变量表示属性受保护，本类以外的代码在访问这样的属性时应该要保持慎重
- 面向对象的三大支柱
  - 封装：隐藏一切可以隐藏的实现细节，只向外界暴露（提供）简单的编程接口
  - 继承
  - 多态

## 练习

### 练习1：定义一个类描述数字时钟

```python
"""
定义一个类描述数字时钟

Version: 1.0.0
Author: Jalan
Date: 2019-05-24
"""

class Clock:
    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法

        :param hour: 小时
        :param minute: 分钟
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def show_time(self):
        """
        显示时间
        """
        return "%02d:%02d:%02d" % (self._hour, self._minute, self._second)

    def run(self):
        """
        走字
        """
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

def main():
    # 12:01
    clock = Clock(0, 1, 0)
    while True:
        # 显示时间
        print(clock.show_time())
        # 走字
        clock.run()

if __name__ == "__main__":
    main()
```

### 练习2：定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法

```python
"""
定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法

Version: 1.0.0
Author: Jalan
Date: 2019-05-25
"""

import math

class Point:
    def __init__(self, x=0, y=0):
        """
        初始化点

        :param x: 坐标 x
        :param y: 坐标 y
        """
        self._x = x
        self._y = y

    def move_to(self, to_x=0, to_y=0):
        """
        移动点

        :param to_x: 要移动到的 x 坐标
        :param to_y: 要移动到的 y 坐标
        """
        self._x = to_x
        self._y = to_y

    def distance(self, to_x=0, to_y=0):
        """
        计算亮点距离

        :param to_x: 另一个点的坐标 x
        :param to_y: 另一个点的坐标 y
        """
        return math.sqrt((to_x - self._x)**2 + (to_y - self._y)**2)

    def __str__(self):
        """
        魔法方法，当 print 对象时就会输出该方法中 return 的数据
        """
        return '(%s, %s)' % (str(self._x), str(self._y))

def main():
    point = Point(1, 2)
    point.move_to(4, 5)
    print(point.distance(4, 6))
    print(point)

if __name__ == "__main__":
    main()
```

知识点：

- `__str__()` 魔法方法：[Python __str__() 方法](https://www.runoob.com/note/41154)

----

说一说开头的那句 We are all consenting adults here。

学习时搜索资料的适合在 [知乎](https://www.zhihu.com/question/20030486) 看到：

> Nothing is really private in python. No class or class instance cankeep you away from all what's inside (this makes introspectionpossible and powerful). Python trusts you. It says "hey, if you wantto go poking around in dark places, I'm gonna trust that you've gota good reason and you're not making trouble."After all, we're all consenting adults here.
> Python中没有东西是真正private的. 任何类和对象都不会阻止你窥探他们的内部，这使得Python的自省异常强大. Python 对你的态度是信任的，它说：“hey，如果你想尝试使用黑魔法，那么放心大胆的去吧，我相信你一定是有自己的理由的，知道自己在干嘛，并且不会捅出篓子，懂得点到为止”话说回来，大家毕竟都是成年人了，懂得为自己的行为负责，都知道自己在干嘛，所以你想干什么我不会拦着你。

看完好感动。编程语言对我们这么信任，那么一定要好好写代码作为回报呀!

Powered By Love~ ❤️

## 其他资料

- [python定义类()中写object和不写的区别](https://www.cnblogs.com/wujingqiao/p/9668583.html)

