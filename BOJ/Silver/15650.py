'''
solution(N, M) :
1) M == 1 일 때 : [1], [2], [3], ..., [N]
2) N == M 일 때 : [1, 2, 3, ..., N]
3)그 외 : solution(N-1, M) + solution(N-1, M-1) 각 요소 뒤에 N 추가
'''

import sys
import copy


def solution(N, M):
    ans = []

    if M == 1:
        for i in range(1, N + 1):
            ans.append([i])
    elif N == M:
        part = []
        for i in range(1, N + 1):
            part.append(i)
        ans.append(part)
    else:
        for i in solution(N - 1, M):
            ans.append(i)

        if M - 1 >= 1:
            for i in solution(N - 1, M - 1):
                part = copy.deepcopy(i)
                part.append(N)
                ans.append(part)

    ans.sort()

    return ans

n, m = map(int, sys.stdin.readline().rstrip().split())

for i in solution(n, m) :
    for j in i :
        print(j, end = " ")
    print()
