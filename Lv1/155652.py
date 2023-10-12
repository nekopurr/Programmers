# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''
    
    for i in list(skip):
        alpha = alpha.replace(i, '')
    
    for w in s:
        answer += alpha[(alpha.find(w) + index) % len(alpha)]
    return answer
