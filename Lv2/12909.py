# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for x in s:
        if x == "(":
            stack.append(x)
        else:
            if stack:
                stack.pop()
            else:
                return False
            
    if stack:
        return False
    return True
