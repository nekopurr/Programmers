# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    miss_score = dict(zip(name, yearning))
    answer = []

    for who in photo:
        add = 0
        for n in who:
            add += miss_score.get(n, 0)
        answer.append(add)

    return answer