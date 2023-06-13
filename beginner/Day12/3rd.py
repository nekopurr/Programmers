# https://school.programmers.co.kr/learn/courses/30/lessons/120851

def solution(my_string):
    result = 0
    for i in my_string:
        if i.isdigit():
            result += int(i)
    return result

def solution2(my_string):
    return sum(int(i) for i in my_string if i.isdigit())