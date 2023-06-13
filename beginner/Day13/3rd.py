# https://school.programmers.co.kr/learn/courses/30/lessons/120888

def solution(my_string):
    return ''.join(sorted(set(my_string), key = lambda x: my_string.index(x)))

def solution2(my_string):
    return ''.join(dict.fromkeys(my_string))