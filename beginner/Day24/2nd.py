# https://school.programmers.co.kr/learn/courses/30/lessons/120885

def solution(bin1, bin2):
    a = int(bin1, 2)
    b = int(bin2, 2)
    return bin(a + b).replace('0b', '')