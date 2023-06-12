# https://school.programmers.co.kr/learn/courses/30/lessons/120845

def solution(box, n):
    dice = 1
    for i in range(3):
        dice *= box[i] // n
    return dice