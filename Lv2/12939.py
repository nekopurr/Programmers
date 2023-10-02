# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    s = s.split(' ')
    s = [int(n) for n in s]
    s.sort()
    return f'{s[0]} {s[-1]}'