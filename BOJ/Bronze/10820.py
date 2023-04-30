# EOF로 입력 종료 처리 (try-except)

while True :
    try :
        lst = list(input())
        ans = [0, 0, 0, 0]  # 소문자, 대문자, 숫자, 공백

        for l in lst :
            if l == ' ' : ans[3] += 1
            else :
                tmp = ord(l)

                if ord('A') <= tmp <= ord('Z') : ans[1] += 1
                elif ord('a') <= tmp <= ord('z') : ans[0] += 1
                else : ans[2] += 1
        print(*ans)
    except EOFError :
        break
        

# 입력 결과가 False 로 처리

import sys
input = sys.stdin.readline

while True :
    lst = list(input())
    if not lst : break
    ans = [0, 0, 0, 0]  # 소문자, 대문자, 숫자, 공백

    for l in lst :
        if l == ' ' : ans[3] += 1
        else :
            tmp = ord(l)

            if ord('A') <= tmp <= ord('Z') : ans[1] += 1
            elif ord('a') <= tmp <= ord('z') : ans[0] += 1
            elif ord('0') <= tmp <= ord('9') : ans[2] += 1
    print(*ans)
