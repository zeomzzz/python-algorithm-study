'''
solution(N, M) 이라고 할 때
1) M == 1 : [1], [2], ... [N]
2) else : solution(N, M-1) 각 요소에 [1, 2, ..., N]를 추가
'''

import sys

def solution(N, M) :
    ans = []

    if M == 1 :
        for i in arr :
            ans.append([i])
    else :
        for i in solution(N, M-1) :
            for j in arr :
                tmp_arr = i[:]
                tmp_arr.append(j)
                ans.append(tmp_arr)

    return ans


n, m = map(int, sys.stdin.readline().rstrip().split())
arr = list(map(int, sys.stdin.readline().rstrip().split()))
arr = sorted(arr)

for i in solution(n, m) :
    i_tmp = list(map(str, i))
    print(' '.join(i_tmp))
