# https://school.programmers.co.kr/learn/courses/30/lessons/120896

def solution(s):
    result = ''
    for i in s:
        if s.count(i) == 1:
            result += i
    return ''.join(sorted(result))