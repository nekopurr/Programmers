# https://school.programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    return "수박" * (n//2) if n % 2 == 0 else "수박" * (n//2) + "수"