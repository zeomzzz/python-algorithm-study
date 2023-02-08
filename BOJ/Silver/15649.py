import copy
import sys

'''
<규칙>

solution(n, m)은 1) + 2) 중 n, m의 범위가 맞는 경우들로 구성됨

1) solution(n-1, m)을 모두 포함
2) solution(n-1, m-1)에서
각 요소(리스트)의 인덱스 0 ~ m에 n을 삽입한 결과
'''

def solution(n, m) :
    ans = []

    if m == 1 : # solution(n, 1)
        for i in range(1, n + 1) :
            ans.append([i])
    elif n - 1 >= m :
        for i in solution(n - 1, m) :
            ans.append(i)

    if m - 1 >= 1 :
        for i in solution(n - 1, m - 1) :
            for j in range(m) :
                k = copy.deepcopy(i)
                k.insert(j, n)
                ans.append(k)

    ans.sort()

    return ans


n, m = map(int, sys.stdin.readline().rstrip().split())

for i in solution(n, m) :
    for j in i :
        print(j, end = " ")
    print()
