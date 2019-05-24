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