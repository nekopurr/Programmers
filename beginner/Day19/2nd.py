# https://school.programmers.co.kr/learn/courses/30/lessons/120913

import re

def solution(my_str, n):
    return re.findall(f'.{{1,{n}}}', my_str)