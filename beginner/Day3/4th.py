# https://school.programmers.co.kr/learn/courses/30/lessons/120813

def solution(n):
    odd_num = []
    for i in range(n + 1):
        if i % 2 != 0:
            odd_num.append(i)
    return odd_num