"""
设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""
import random

def generate_code(code_length=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码长度（默认 4 个字符）

    :return: 由大小写英文字母和数字构成的随机验证码
    """
    # 大写字母
    upper_list = [chr(x) for x in range(ord('A'), ord('A') + 26)]    
    #print(upper_list)
    # 小写字母
    lower_list = [chr(x) for x in range(ord('a'), ord('a') + 26)]
    #print(lower_list)
    # 0-9 数字
    digit_list = [x for x in range(0, 10)]
    #print(digit_list)
    res_list = upper_list + lower_list + digit_list
    res_list_len = len(res_list)
    code = ''
    for _ in range(code_length):
        index = random.randint(0, res_list_len - 1)
        code += res_list[index]
    return code

def main():
    code_len = int(input('请输入验证码长度：'))
    print(generate_code(code_len))

if __name__ == '__main__':
    main()