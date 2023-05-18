# https://school.programmers.co.kr/learn/courses/30/lessons/120824

def solution(num_list):
    odd = 0
    even = 0
    for i in num_list:
        if i % 2 == 0:
            even += 1
        elif i % 2 == 1:
            odd += 1
    return [even, odd]