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