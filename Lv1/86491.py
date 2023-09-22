# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    max_a = 0
    max_b = 0

    for a, b in sizes:
        if a < b:
            a, b = b, a
        max_a = max(max_a, a)
        max_b = max(max_b, b)

    return max_a * max_b