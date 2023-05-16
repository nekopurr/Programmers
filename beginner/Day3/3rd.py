# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    dict = {}

    for i in range(max(array) + 1):
        dict[i] = array.count(i)

    dict_max = max(dict, key=dict.get)
    dict_multiple = len([i for i, j in dict.items() if max(dict.values()) == j])

    if dict_multiple > 1:
        return -1
    else:
        return dict_max