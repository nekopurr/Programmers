# https://school.programmers.co.kr/learn/courses/30/lessons/120835

def solution(emergency):
    emergency_sorted = sorted(emergency, reverse=True)
    answer = []

    for i in emergency:
        answer.append(emergency_sorted.index(i) + 1)

    return answer