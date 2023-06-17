# https://school.programmers.co.kr/learn/courses/30/lessons/120894

def solution(numbers):
    l = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i, n in enumerate(l):
        numbers = numbers.replace(n, str(i))

    return int(numbers)