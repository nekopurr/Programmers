# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def divisors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return 1 if count % 2 == 0 else -1


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        answer += i * divisors(i)
    return answer