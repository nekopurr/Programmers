# https://school.programmers.co.kr/learn/courses/30/lessons/120849

def solution(my_string):
    l = ['a', 'e', 'i', 'o', 'u']
    for i in l:
        my_string = my_string.replace(i, '')
    return my_string