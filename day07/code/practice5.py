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
