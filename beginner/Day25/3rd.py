# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    n = 0
    for i in range(1, num):
        n += i
    start = (total - n) // num
    return [i for i in range(start, start + num)]