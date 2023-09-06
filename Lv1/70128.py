# https://school.programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    answer = []
    for i in range(len(a)):
        answer.append(a[i] * b[i])
    return sum(answer)