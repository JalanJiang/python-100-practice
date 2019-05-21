"""
打印各种三角形图案

*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Version: 0.1
Author: Jalan
Date: 2019-05-21
"""

row = int(input("请输入行数："))

# 第一种三角形：第 x 行打印出 x 个星号
for i in range(row):
    for _ in range(i + 1):
        print("*", end="")
    print()

# 第二种三角形：第 x 行打印 row - x 个空格和 x 个星号
for i in range(row):
    row_num = i + 1
    space = row - row_num

    for _ in range(space):
        print(" ", end="")
    
    for _ in range(row_num):
        print("*", end="")
    
    print()

# 第三种三角形：每一行的星号数量是 1, 3, 5, 7, 9......

# 最后一行星号数量
max_num = 2 * row - 1

for i in range(row):
    row_num = i + 1
    # 当前行星号数量
    star_num = row_num * 2 - 1
    # 当前行左右分别存在空格数量
    space = int((max_num - star_num) / 2)

    for _ in range(space):
        print(" ", end="")
    
    for _ in range(star_num):
        print("*", end="")

    print()