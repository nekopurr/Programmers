# https://school.programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    result = []
    correct = 0
    for num in lottos:
        if num in win_nums:
            correct += 1

    if 7-correct-lottos.count(0) > 6:
        result.append(6)
    else:
        result.append(7 - correct - lottos.count(0))

    if 7-correct > 6:
        result.append(6)
    else:
        result.append(7-correct)
    return result