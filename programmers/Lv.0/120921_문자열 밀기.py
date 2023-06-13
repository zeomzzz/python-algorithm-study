def solution(A, B):
    answer = 0
    tmp_A = A
    pushed_A = ''

    # 1) A == B
    if A == B :
        return answer
    # 2) A != B
    else :
        while True :
            pushed_A = tmp_A[len(A) - 1] # 마지막 문자 맨 앞으로

            for i in range(0, len(A) - 1) : # 이 외의 문자 한 칸 씩 오른쪽으로
                pushed_A += tmp_A[i]

            tmp_A = pushed_A
            answer += 1 # 밀기 한 바퀴 끝나면 answer + 1 하여 몇 번 밀었는지

            if pushed_A == B : # 밀어서 B 되면 종료
                break
            elif answer == len(A) : # 처음으로 돌아올 때까지 밀었는데 B 안되면 -1
                answer = -1
                break
    
    return answer
