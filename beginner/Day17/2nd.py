# https://school.programmers.co.kr/learn/courses/30/lessons/120905

def solution(n, numlist):
    return [i for i in numlist if i % n == 0]

def solution2(n, numlist):
    return list(filter(lambda x: x%n==0, numlist))