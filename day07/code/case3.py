"""
井字棋

Version: 1.0.0
Author: Jalan
Date: 2019-05-23
"""

import os

def print_board(board):
    """
    画格子

    :param board: 每个格子的内容
    """
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def is_winner(board, turn):
    """
    判断走棋者是否是赢家

    :param board: 当前棋盘数据
    :param turn: 走棋者
    :return 走棋者是赢家返回 True，否则返回 False
    """
    return ((board['TL'] == turn and board['TM'] == turn and board['TR'] == turn) or
    (board['ML'] == turn and board['MM'] == turn and board['MR'] == turn) or
    (board['BL'] == turn and board['BM'] == turn and board['BR'] == turn) or
    (board['TL'] == turn and board['ML'] == turn and board['BL'] == turn) or
    (board['TM'] == turn and board['MM'] == turn and board['BM'] == turn) or
    (board['TR'] == turn and board['MR'] == turn and board['BR'] == turn) or
    (board['TL'] == turn and board['MM'] == turn and board['BR'] == turn) or
    (board['BL'] == turn and board['MM'] == turn and board['TR'] == turn))

def main():
    # 初始化一个空棋盘
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    # print_board(init_board)

    begin = True
    
    while begin:
        # 开始一盘新棋局
        current_board = init_board.copy()
        begin = False

        # 轮到 x 走
        turn = 'x'
        # 已经走了几个格子
        counter = 0

        # 清屏
        os.system('clear')

        print_board(current_board)

        while counter < 9:
            move = input('轮到 %s 走，请输入位置：' % turn)
            if current_board[move] == ' ':
                counter += 1
                current_board[move] = turn

                if is_winner(current_board, turn):
                    print("产生赢家：%s 赢得胜利" % turn)
                    break

                turn = 'o' if turn == 'x' else 'x'

            os.system('clear')
            print_board(current_board)

        choice = input('是否再玩一局？(y/n)')
        begin = choice == 'y'


if __name__ == "__main__":
    main()