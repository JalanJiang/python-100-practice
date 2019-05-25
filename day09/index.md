# Day09 - 面向对象进阶

## @property 装饰器

- 防止私有变量在外部被随意访问和修改，避免写复杂的 setter 和 getter 方法
- 负责把一个方法变成属性调用
- 关键字
    - `@property`
    - `@name.setter`
  
```python
class Person:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, age):
        self._age = age

def main():
    person = Person('Jalan', 18)
    person.name = 'Jay'
```

参考：[使用@property](https://www.liaoxuefeng.com/wiki/897692888725344/923030547069856)

## __slots__ 魔法

- 限定自定义类型的对象只能绑定某些属性
- 只对当前类的对象生效，对子类并不起任何作用

```python
class Person:
    # Person 类只能绑定 _name 和 _age 属性
    __slots__ = ('_name', '_age')
```

## 静态方法和类方法

### 静态方法

众所周知，静态方法属于类而不属于对象。在之前的编程过程中，如果调用一个方法时不想 new 一个对象出来，我就会把它定义成静态方法（粗暴），但始终不知道要定义静态方法的真正时机是什么。

骆昊老师的教程里举了个例子，算是看明白了：

> 我们写在类中的方法并不需要都是对象方法，例如我们定义一个“三角形”类，通过传入三条边长来构造三角形，并提供计算周长和面积的方法，但是传入的三条边长未必能构造出三角形对象，因此我们可以先写一个方法来验证三条边长是否可以构成三角形，这个方法很显然就不是对象方法，因为在调用这个方法时三角形对象尚未创建出来（因为都不知道三条边能不能构成三角形），所以这个方法是属于三角形类而并不属于三角形对象的。

定义静态方法关键字：`@staticmethod`

### 类方法

- `@classmethod`
- `cls` 表示类本身
- 通过 `cls` 可以获取和类相关的信息并且可以创建出类的对象

```python
class Clock:

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        # 返回一个类对象
        return cls(1, 2, 3)
```

## 类之间的关系

- is-a：继承或泛化
- has-a：关联。例如部门和员工的关系
- use-a：依赖。例如方法中使用到某个其他对象

## 继承和多态

- 子类比父类拥有更多的功能。用子类对象替换一个父类对象，[里氏替换原则](https://zh.wikipedia.org/wiki/%E9%87%8C%E6%B0%8F%E6%9B%BF%E6%8D%A2%E5%8E%9F%E5%88%99)
- 继承的写法：`class Teacher(Person)`，和其他编程语言不同，没有什么 `extends` 关键字，而是直接在类后的括号里标明所要继承的父类
- 子类对父类已有方法给出新的实现版本：重写（override）。当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）
- 顺便复习：重载是指相同函数名的不同使用方式，Python 中没有重载

### 抽象类

- Python 在语法层面没有像 Java 或 C# 那样提供对抽象类的支持
- 但可以通过 abc 模块的 ABCMeta 元类和 abstractmethod 包装器来达到抽象类的效果
- 如果一个类中存在抽象方法那么这个类就不能够实例化（创建对象）

```python
from abc import ABCMeta, abstractmethod


class Pet(object, metaclass=ABCMeta):
    """宠物"""

    def __init__(self, nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass


class Dog(Pet):
    """狗"""

    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
    """猫"""

    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)


def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        # make_voice 表现出了多态行为
        pet.make_voice()


if __name__ == '__main__':
    main()
```

## 综合案例

### 案例1：奥特曼打小怪兽

大概看了一下代码，描述一下这个案例。

首先需要定义一个攻击者类 `Fighter`，奥特曼和小怪兽都是攻击者。攻击者的基本属性有姓名 `name` 和生命值 `hp`。

- 奥特曼：
  - 90% 概率使用普通攻击。普通攻击打一拳 hp-10
  - 10% 概率使用魔法攻击，但魔法攻击需要蓄力，蓄力值达到 100 才可以发动。每回合可以恢复蓄力值 10 点。魔法攻击打一拳 hp-50
- 小怪兽：
  - 只会普通攻击，每一回合结束奥特曼会被所有小怪兽打一拳，打一拳 hp-5
- 琦玉老师：
  - 每回合除奥特曼出击外有 1% 的概率召唤琦玉老师，一拳解决一只小怪兽

```python
"""
奥特曼打小怪兽

Version: 1.0.0
Author: Jalan
Date: 2019-05-25
"""

from abc import ABCMeta, abstractclassmethod
from random import randint, randrange
import time

class Fighter(metaclass=ABCMeta):
    """
    攻击者
    """

    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        """
        初始化攻击者

        :param name: 攻击者姓名
        :param hp: 攻击者 hp
        """
        self._name = name
        self._hp = hp

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp > 0 else 0

    def is_alive(self):
        """
        判断是否存活

        :return 如果存活返回 True，否则返回 False
        """
        return True if self._hp > 0 else False

    @abstractclassmethod
    def attack(self, other):
        """
        普通攻击

        :param other: 攻击对象
        """
        pass
    
class Ultraman(Fighter):
    """
    奥特曼
    """

    __slots__ = ('_name', '_hp', '_mp')

    def __init__(self, name, hp):
        """
        初始化奥特曼

        :param name: 奥特曼名字
        :param hp: 奥特曼 hp
        :param mp: 奥特曼魔法蓄力值
        """
        super().__init__(name, hp)
        self._mp = 100

    def attack(self, other):
        """
        普通攻击一拳 -10
        """
        num = randint(1, 10)
        if num == 1:
            self._magic_attack(other)
        else:
            other.hp -= 10
        

    def _magic_attack(self, other):
        """
        魔法攻击

        :param other: 攻击对象
        """
        if self._mp == 100:
            other.hp -= 50
            return True
        else:
            return False

    def resume_mp(self):
        """
        恢复 mp
        """
        if self._mp < 100:
            self._mp += 10

    def __str__(self):
        return '奥特曼 %s 生命值 %s' % (self._name, self._hp)

class OnePunchMan(Fighter):
    """
    琦玉老师
    """

    __slots__ = ('_name', '_hp')

    def __init__(self, name):
        """
        初始化一个一拳超人
        """
        self._name = name
        self._hp = float('inf')

    def attack(self, other):
        """
        一拳打死

        :param other: 攻击对象
        """
        other._hp = 0

    def __str__(self):
        return '琦玉老师出场'

class Monster(Fighter):
    """
    小怪兽
    """

    __slots__ = ('_name', '_hp', '_hurt')

    def __init__(self, name, hp):
        """
        初始化小怪兽
        """
        self._name = name
        self._hp = hp
        

    def attack(self, other):
        """
        普通攻击
        """
        other.hp -= 5

    def __str__(self):
        return '小怪兽 %s 生命值 %s' % (self._name, self._hp)


def is_any_alive(monsters):
    """
    是否还有小怪兽存活

    :return 是返回 True，否返回 False
    """
    for monster in monsters:
        if monster.is_alive:
            return True
    return False

def select_monster(monsters):
    """
    选择一只小怪兽

    :return 返回小怪兽
    """
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.is_alive:
            return monster

def main():
    u = Ultraman('迪迦', 500)
    m1 = Monster('小龙虾', 100)
    m2 = Monster('大螃蟹', 120)
    m3 = Monster('老乌龟', 200)
    monsters = [m1, m2, m3]
    one = OnePunchMan('琦玉老师')

    while u.is_alive and is_any_alive(monsters):
        target = select_monster(monsters)
        # 小怪兽被打
        u.attack(target)

        # 小怪兽打奥特曼
        for monster in monsters:
            if monster.is_alive:
                monster.attack(u)

        # 判断是否可以召唤琦玉老师
        one_punc_num = randint(1, 100)
        if one_punc_num == 1 and is_any_alive(monsters):
            target = select_monster(monsters)
            one.attack(target)
            print(one)

        print(target)
        print(u)

        time.sleep(2)
        
if __name__ == "__main__":
    main()
```