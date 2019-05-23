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
