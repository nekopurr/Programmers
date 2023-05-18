# https://school.programmers.co.kr/learn/courses/30/lessons/120831

def solution(n):
    l = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            l.append(i)
    return sum(l)