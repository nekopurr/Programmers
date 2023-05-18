# https://school.programmers.co.kr/learn/courses/30/lessons/120816

def solution(slice, n):
    a = slice
    while True:
        if slice >= n:
            return slice // a
        else:
            slice += a