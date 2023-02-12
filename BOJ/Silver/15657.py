'''
solution(N, M, Arr) 이라고 할 때
1) M == 1 : [1], [2], ... [N]
2) else : solution(N, M-1) 각 요소에 [1, 2, ..., N] 중
solution(N, M-1)의 맨 끝(최대값)보다 크거나 같은 정수를 추가
'''

import sys

def solution(N, M, Arr) :
    ans = []
    arr = sorted(Arr)
    arr_max = arr[-1]

    if M == 1 :
        for i in arr :
            ans.append([i])
    else :
        for i in solution(N, M-1, Arr) :
            for j in arr :
                if j >= i[-1] :
                    tmp = i[:]
                    tmp.append(j)
                    ans.append(tmp)

    return ans

n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for i in solution(n, m, arr) :
    i_tmp = list(map(str, i))
    print(' '.join(i_tmp))
