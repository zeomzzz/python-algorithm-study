'''
풀이 1 : 재귀

solution(N, M) 일 때,
1) M == 1 이면 : [1], [2], [3], ..., [N]
2) 그 외의 경우 : solution(N, M-1) 요소 각각에 1 ~ N을 한 번 씩 추가함
'''

import sys

def solution(N, M):
    # N : 자연수 범위 1 ~ N
    # M : 고르는 개수 (M개)
    ans = []

    if M == 1 :
        for i in range(1, N+1) :
            ans.append([i])
    else :
        for i in solution(N, M-1) :
            for j in range(1, N+1) :
                tmp = i[:]
                tmp.append(j)
                ans.append(tmp)

    return ans

n, m = map(int, sys.stdin.readline().rstrip().split())

for i in solution(n, m) :
    for j in i :
        print(j, end=" ")
    print()
