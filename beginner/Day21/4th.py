# https://school.programmers.co.kr/learn/courses/30/lessons/120878

def solution(spell, dic):
    for i in dic:
        if not set(spell) - set(i):
            return 1
    return 2