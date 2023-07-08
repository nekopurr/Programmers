# https://school.programmers.co.kr/learn/courses/30/lessons/120861

def solution(keyinput, board):
    board_x = board[0] // 2
    board_y = board[1] // 2
    where = [0, 0]

    for i in keyinput:
        if i == 'left':
            if where[0] == -board_x:
                pass
            else:
                where[0] -= 1
        if i == 'right':
            if where[0] == board_x:
                pass
            else:
                where[0] += 1
        if i == 'up':
            if where[1] == board_y:
                pass
            else:
                where[1] += 1
        if i == 'down':
            if where[1] == -board_y:
                pass
            else:
                where[1] -= 1

    return where