# https://school.programmers.co.kr/learn/courses/30/lessons/120829

def solution(angle):
    if angle == 180:
        return 4
    elif angle > 90:
        return 3
    elif angle == 90:
        return 2
    elif angle < 90:
        return 1


def solution1(angle):
    return (angle // 90) * 2 + (angle % 90 > 0) * 1
