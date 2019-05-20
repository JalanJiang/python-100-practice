# Day01 - 初识Python

## Python 简介

- Python 3.x 的很多新特性后来也被移植到 Python 2.6/2.7 版本中
- 多行注释 - 三个引号开头，三个引号结尾
- [Anaconda](https://baike.baidu.com/item/anaconda/20407441?fr=aladdin) 是一个开源的 Python 发行版本，其包含了 conda、Python 等 180 多个科学包及其依赖项

## Python 环境

### 安装交互式工具

```
$ pip3 install ipython jupyter
```

----

## 作业

### 1. Python 之禅

启动 IPython：

```
$ ipython
```

启动后输入 `import this` 会看到以下输出：

```python
In [1]: import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

搜索了一下才知道这是一个 Python 的彩蛋，也被称作“Python 之禅”。

下面按照作业要求做下翻译：

```
Beautiful is better than ugly.
优美胜于丑陋。

Explicit is better than implicit.
明了胜于晦涩。

Simple is better than complex.
简洁胜于复杂。

Complex is better than complicated.
复杂胜于凌乱。

Flat is better than nested.
扁平胜于嵌套。

Sparse is better than dense.
间隔胜于紧凑。

Readability counts.
可读性非常重要。

Special cases aren't special enough to break the rules.
Although practicality beats purity.
即便假借特例的实用性之名，也不可违背这些规则。

Errors should never pass silently.
Unless explicitly silenced.
不要包容所有错误，除非你确定需要这样做。（这里指的是异常捕获）

In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
当存在多种可能，不要尝试去猜测，而是尽量找一种，最好是唯一一种明显的解决方案。

Although that way may not be obvious at first unless you're Dutch.
尽管这一开始并不容易，毕竟你不是 Python 之父。

Now is better than never.
Although never is often better than *right* now.
做也许好过不做，但不假思索就动手还不如不做。

If the implementation is hard to explain, it's a bad idea.
如果你无法向人描述你的方案，那肯定不是一个好方案。

If the implementation is easy to explain, it may be a good idea.
如果你的方案易于描述，那么这可能是一个好的方案。

Namespaces are one honking great idea -- let's do more of those!
命名空间是一个绝妙的理念，我们应当多加利用。
```

### 2. turtle 绘制图形

turtle 是 Python 中内置的简单绘图工具，名字也很萌，叫做海龟绘图（Turtle Graphics）。

详细教程可见 [10分钟轻松学会 Python turtle 绘图](https://www.cnblogs.com/nowgood/p/turtle.html)。

```Python
import turtle

# 设置画笔宽度
turtle.pensize(4)
# 设置画笔颜色
turtle.pencolor('red')
# 向当前画笔方向移动 100 像素长
turtle.forward(100)
# 顺时针移动 90 度
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.mainloop()
```

画图结果：

![学习使用 turtle 在屏幕上绘制图形](/img/day01/task-2.png)

----

## 练习

