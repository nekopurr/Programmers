# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = []
    s = s.split(' ')
    for i in s:
        i = i.capitalize()
        answer.append(i)
    return ' '.join(answer)
