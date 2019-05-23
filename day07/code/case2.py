"""
约瑟夫问题

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""

def main():
    # 初始化，还没被扔掉的标为 True
    persons = [True for _ in range(30)]
    count, index, number = 0, 0, 0
    while count < 15:
        if persons[index]:
            number += 1 # 计数
            if number == 9:
                # 被扔掉
                persons[index] = False
                # 扔掉的人数 + 1
                count += 1
                # 重新开始计数
                number = 0
        index += 1
        index %= 30
    
    for person in persons:
        print('是基督徒' if person else '不是基督徒')

if __name__ == "__main__":
    main()