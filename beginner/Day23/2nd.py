# https://school.programmers.co.kr/learn/courses/30/lessons/120882

def solution(score):
    avg = []
    result = []
    for i in score:
        avg.append((i[0] + i[1]) / 2)
    sorted_avg = sorted(avg, reverse=True)

    for i in avg:
        result.append(sorted_avg.index(i) + 1)

    return result