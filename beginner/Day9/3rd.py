# https://school.programmers.co.kr/learn/courses/30/lessons/120839

def solution(rsp):
    rsp_dict = {'2': '0', '0': '5', '5': '2'}
    return ''.join(rsp_dict[i] for i in rsp)