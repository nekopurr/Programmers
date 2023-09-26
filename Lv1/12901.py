# https://school.programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    answer = 0

    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']

    for i in range(a-1):
        answer += months[i]

    answer += b - 1

    return days[answer % 7]