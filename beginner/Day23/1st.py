# # https://school.programmers.co.kr/learn/courses/30/lessons/120880

def solution(numlist, n):
    result = sorted(numlist, key = lambda x:(abs(x-n), n-x))
    return result