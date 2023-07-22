# https://school.programmers.co.kr/learn/courses/30/lessons/120956

import re

def solution(babbling):
    count = 0
    p = r'^(aya|ye|woo|ma)+$'

    for w in babbling:
        if re.search(p, w):
            count += 1
            
    return count