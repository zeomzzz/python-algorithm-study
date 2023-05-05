'''
1. 아이디어
- 백트래킹 이용해서 가능한 모든 순서로 정수를 담기
- 한 가지 방법으로 담을 때마다 최댓값 구하기
2. 시간복잡도
- N!
3. 자료구조
- boolean[] : 정수 담았는지 체크
- int[] : 배열 만들기
'''

import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
res = [0] * N # 정수 정렬해서 넣을 리스트
visited = [0] * N # 방문체크
ans = 0

def cal(lst) :
    global N
    result = 0

    for i in range(0, N - 1) :
        result += abs(lst[i] - lst[i + 1])

    return result

def backtracking(res, visited, depth) :
    global ans

    # base
    if depth == N :
        ans = max(ans, cal(res))
        return

    # recursive
    for i in range(N) :
        if not visited[i] :
            res[depth] = A[i]
            visited[i] = 1

            # 다음 깊이 탐색
            backtracking(res, visited, depth + 1)

            # 원복
            res[depth] = 0
            visited[i] = 0

backtracking(res, visited, 0)

print(ans)
