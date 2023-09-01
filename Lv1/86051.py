# https://school.programmers.co.kr/learn/courses/30/lessons/86051

def solution(numbers):
    all = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return sum([x for x in all if x not in numbers])