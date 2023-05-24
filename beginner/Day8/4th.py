# https://school.programmers.co.kr/learn/courses/30/lessons/120836
'''
def solution(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    return cnt
'''

def solution(n):
    return len(list(filter(lambda x: n % (x + 1) == 0, range(n))))