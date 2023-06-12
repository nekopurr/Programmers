# https://school.programmers.co.kr/learn/courses/30/lessons/120846

def solution(n):
    count = 0
    for i in range(1, n + 1):
        if divisor_count(i) >= 3:
            count += 1
    return count


def divisor_count(n):
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return len(l)