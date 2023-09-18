# https://school.programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = ''

    while n > 0:			
        n, r = divmod(n, 3)
        answer += str(r)
    return int(answer, 3)
