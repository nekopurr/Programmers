# https://school.programmers.co.kr/learn/courses/30/lessons/120904

def solution(num, k):
    return -1 if str(num).find(str(k)) == -1 else str(num).find(str(k)) + 1