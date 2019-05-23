"""
在屏幕上显示跑马灯文字
打印一段文字，休眠，清理屏幕，打印……

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""
import os
import time

def main():
    content = "今天是个好日子啊……"
    while True:
        os.system('clear')
        print(content)

        # 休眠
        time.sleep(0.2)
        # 制造跑马灯效果
        content = content[1:] + content[0]
    
if __name__ == "__main__":
    main()