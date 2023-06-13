def solution(polynomial):
    a = 0
    b = 0
    
    pol_split = polynomial.split(' + ')
    pol_split = sorted(pol_split, reverse = True)
    
    # 동류항끼리 계산 (x의 계수 1인 경우 주의)
    for i in pol_split :
        if 'x' in i :
            if i.replace('x', '') == '' :
                i = '1x'
            a += float(i.replace('x', ''))
        else :
            b += float(i)
    
    # 정수인 경우 실수 -> 정수
    if int(a) == a :
        a = int(a)
    if int(b) == b :
        b = int(b)
    
    # ax + b 형태로 answer 반환 (x의 계수 1인 경우 주의)
    if a != 0 and b != 0 :
        if a == 1 :
            answer = 'x + ' + str(b)
        else :
            answer = str(a) + 'x + ' + str(b)
    elif a != 0 and b == 0 :
        if a == 1 :
            answer = 'x'
        else :
            answer = str(a) + 'x'
    elif a == 0 and b != 0 :
        answer = str(b)

    return answer
