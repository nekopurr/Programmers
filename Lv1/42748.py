# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []

    for a, b, c in commands:
        sorted_slice_array = sorted(array[a-1:b])
        answer.append(sorted_slice_array[c-1])

    return answer