# https://school.programmers.co.kr/learn/courses/30/lessons/120815

def solution(n):
    a = 1
    while True:
        if (n * a) % 6 == 0:
            return (n * a) // 6
        else:
            a += 1