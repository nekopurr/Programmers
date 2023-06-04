# https://school.programmers.co.kr/learn/courses/30/lessons/120841

def solution(dot):
    if dot[0] < 0:
        answer = 2
        if dot[1] < 0:
            answer += 1
    else:
        answer = 1
        if dot[1] < 0:
            answer += 3
    return answer