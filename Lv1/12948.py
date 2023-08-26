# https://school.programmers.co.kr/learn/courses/30/lessons/12948

import re

def solution(phone_number):
    p = r'\w'
    answer = re.sub(p, '*', phone_number[:-4])
    return answer + ''.join(list(phone_number)[-4:])