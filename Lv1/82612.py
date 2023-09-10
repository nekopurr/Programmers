# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    n = 0
    for i in range(1, count + 1):
        n += i * price
    if money < n:
        return n - money
    else:
        return 0