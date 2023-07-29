# https://school.programmers.co.kr/learn/courses/30/lessons/120884

def solution(chicken):
    coupon = chicken
    answer = 0

    while coupon >= 10:
        count = coupon // 10
        answer += count
        coupon = coupon % 10 + count

    return answer