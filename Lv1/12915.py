# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x:x[n])
