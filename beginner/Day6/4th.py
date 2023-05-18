# https://school.programmers.co.kr/learn/courses/30/lessons/120825

def solution(my_string, n):
    a = []
    for i in range(len(my_string)):
        a.append(my_string[i] * n)
    return ''.join(a)