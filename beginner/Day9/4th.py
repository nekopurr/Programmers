# https://school.programmers.co.kr/learn/courses/30/lessons/120840

def solution(balls, share):
    return fac(balls) / (fac(balls - share) * fac(share))

def fac(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result