# https://school.programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    num = n ** 0.5
    if num == int(num):
        return (num + 1) ** 2
    else:
        return -1