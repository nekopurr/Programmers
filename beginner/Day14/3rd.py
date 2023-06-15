# https://school.programmers.co.kr/learn/courses/30/lessons/120892

def solution(cipher, code):
    result = ''
    for i in range(1, len(cipher) // code + 1):
        result += cipher[(i * code) - 1]
    return result