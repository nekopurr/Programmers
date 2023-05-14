# https://school.programmers.co.kr/learn/courses/30/lessons/120808

def solution(numer1, denom1, numer2, denom2):
    denom_mul = denom1 * denom2
    numer1 *= denom2
    numer2 *= denom1

    result = []
    answer = []
    result.append(numer1 + numer2)
    result.append(denom_mul)

    def gcd(a, b):
        while b > 0:
            a, b = b, a % b
        return a

    answer.append(result[0] // (gcd(result[0], result[1])))
    answer.append(result[1] // (gcd(result[0], result[1])))
    return answer