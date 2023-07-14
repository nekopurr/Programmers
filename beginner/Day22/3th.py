# https://school.programmers.co.kr/learn/courses/30/lessons/120876

def solution(lines):
    l = []

    for i in range(3):
        a, b = lines[i][0], lines[i][1]
        for j in range(a, b):
            l.append(j)
    return len(set([x for x in l if l.count(x) > 1]))