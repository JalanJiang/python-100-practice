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