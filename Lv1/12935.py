# https://school.programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    if len(arr) == 1:
        arr = [-1]
    else:
        arr.remove(min(arr))

    return arr