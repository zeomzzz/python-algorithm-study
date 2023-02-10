'''
재귀를 이용한 풀이

solution(N, M) 이라고 할 때
1) M == 1 이면 :[1], [2], ... [N]
2) else : f(N, M-1) 각 요소(리스트)에 해당 리스트의 마지막 요소(정수) ~ N 인 수를 추가한 리스트
'''

import sys

def solution(N, M) :
    ans = []

    if M == 1 :
        for i in range(1, N+1) :
            ans.append([i])

    else :
        for lst in solution(N, M-1) :
            for j in range(lst[-1], N+1) :
                part_lst = lst[:]
                part_lst.append(j)
                ans.append(part_lst)

    return ans

n, m = map(int, sys.stdin.readline().rstrip().split())

for lst in solution(n, m) :
    tmp_lst = list(map(str, lst))
    print(' '.join(tmp_lst))
