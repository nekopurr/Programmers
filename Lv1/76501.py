# https://school.programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    for i in list(zip(absolutes, signs)):
        if i[1] == True:
            answer += i[0]
        elif i[1] == False:
            answer -= i[0]
    return answer