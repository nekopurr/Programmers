# https://school.programmers.co.kr/learn/courses/30/lessons/120852

def solution(n):
    div = 2
    l = []
    while div <= n:
        if n % div != 0:
            div += 1
            continue
        n /= div
        l.append(div)
    return sorted(list(set(l)))