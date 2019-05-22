"""
判断一个数是不是回文数的函数

Version: 1.0.0
Author: Jalan
Date: 2019-05-22
"""

def is_palindrome(num):
    num_string = str(num)
    i = 0
    j = len(num_string) - 1

    while i <= j:
        left = num_string[i]
        right = num_string[j]
        if left != right:
            return False
        i += 1
        j -= 1
        
    return True

n = int(input("输入数字："))
print(is_palindrome(n))