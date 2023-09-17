# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        if i == 0:
            answer.append(int(arr[i]))
        elif arr[i] != arr[i-1]:
            answer.append(int(arr[i]))
    
    return answer
