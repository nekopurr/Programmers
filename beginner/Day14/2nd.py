# https://school.programmers.co.kr/learn/courses/30/lessons/120891

import re

def solution(order):
    p = re.compile('[369]')
    return len(p.findall(str(order)))