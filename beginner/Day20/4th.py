# https://school.programmers.co.kr/learn/courses/30/lessons/120863

def solution(polynomial):
    x = 0
    num = 0
    for i in polynomial.split(' + '):
        if i.isdigit():
            num += int(i)
        elif i[-1] == 'x':
            x += 1 if len(i) == 1 else int(i[:-1])

    if x == 0:
        return str(num)
    elif x == 1:
        return 'x + ' + str(num) if num != 0 else 'x'
    else:
        return f'{x}x + {num}' if num != 0 else f'{x}x'