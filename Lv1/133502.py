# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    result = 0
    l = []
    for i in ingredient:
        l.append(i)
        if l[-4:] == [1, 2, 3, 1]:
            result += 1
            for _ in range(4):
                l.pop()
    return result