# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    n = len(s)
    return s[n//2] if n % 2 == 1 else s[n//2-1] + s[n//2]