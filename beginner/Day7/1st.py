# https://school.programmers.co.kr/learn/courses/30/lessons/120826

import re

def solution(my_string, letter):
    return re.sub(letter, '', my_string)