# https://school.programmers.co.kr/learn/courses/30/lessons/120834

def solution(age):
    result = ''
    age = str(age)
    for i in age:
        result += chr((int(i)+97))
    return result