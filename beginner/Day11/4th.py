# https://school.programmers.co.kr/learn/courses/30/lessons/120848

def solution(n):
    count = 1
    num = 1
    while True:
        if count * num <= n:
            count *= num
            num += 1
        else:
            break
    return num - 1