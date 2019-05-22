"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 1.0.0
Author: Jalan
Date: 2019-05-22
"""
import random

def getRandomNum():
    num = random.randint(1, 6) + random.randint(1, 6)
    print("摇骰子点数为 %d" % num)
    return num

money = 1000
count = 1

while money > 0:
    print("第 %d 局开始，您的赌注为 %d 元" % (count, money))

    while True:
        debt = int(input('请下注: '))
        if debt > 0 and debt <= money:
            break

    first_num = getRandomNum()
    if first_num == 7 or first_num == 11:
        money += debt
        print("本轮结束，玩家胜")
    elif first_num == 2 or first_num == 3 or first_num == 12:
        money -= debt
        print("本轮结束，庄家胜")
    else:
        second_num = getRandomNum()
        if second_num == 7:
            money -= debt
            print("本轮结束，庄家胜")
        elif second_num == first_num:
            money += debt
            print("本轮结束，玩家胜")
        else:
            print("本轮结束，未分出胜负")
        
    count += 1

print("游戏结束，您身无分文")
    

