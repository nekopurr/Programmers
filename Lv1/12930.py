# https://school.programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    s = s.split(" ")

    for x in range(len(s)):
        s_list = list(s[x])

        for i in range(len(s_list)):
            if i % 2 == 0:
                s_list[i] = s_list[i].upper()
            elif i % 2 == 1:
                s_list[i] = s_list[i].lower()
        s[x] = ''.join(s_list)

    return ' '.join(s)