# https://school.programmers.co.kr/learn/courses/30/lessons/120887

import re

def solution(i, j, k):
    text = ''
    for n in range(i, j + 1):
        text += str(n)

    p = re.compile(str(k))
    answer = p.findall(text)

    return len(answer)