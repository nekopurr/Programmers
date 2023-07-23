# https://school.programmers.co.kr/learn/courses/30/lessons/120878

from math import gcd

def solution(a, b):
    b //= gcd(a,b)
    while b % 5 == 0:
        b //= 5
    while b % 2 == 0:
        b //= 2
    return 1 if b == 1 else 2