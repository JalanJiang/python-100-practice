"""
练习6：打印杨辉三角

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""

def main():
    row = int(input('输入行数：'))

    # 初始化列表
    yh_triangle = [[] for _ in range(row)]

    for i in range(row):
        if i == 0:
            yh_triangle[i] = [1]
        elif i == 1:
            yh_triangle[i] = [1, 1]
        else:
            yh_triangle[i].append(1)
            for j in range(1, len(yh_triangle[i - 1])):
                yh_triangle[i].append(yh_triangle[i - 1][j] + yh_triangle[i - 1][j - 1])
            yh_triangle[i].append(1)
        print(yh_triangle[i], end="\n")


if __name__ == '__main__':
    main()