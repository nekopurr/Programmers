# https://school.programmers.co.kr/learn/courses/30/lessons/81301

import re

def solution(s):
    mapping = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for word, digit in mapping.items():
        s = re.sub(word, digit, s)

    return int(s)