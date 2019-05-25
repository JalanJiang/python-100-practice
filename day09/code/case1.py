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