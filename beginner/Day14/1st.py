# https://school.programmers.co.kr/learn/courses/30/lessons/120890

def solution(array, n):
    array.append(n)
    array.sort()
    n_index = array.index(n)
    a, b = 0, 0
    if array[0] == n:
        return array[1]
    elif array[-1] == n:
        return array[-2]
    else:
        a = n - array[n_index - 1]
        b = array[n_index + 1] - n

    if a > b:
        return array[n_index + 1]
    else:
        return array[n_index - 1]