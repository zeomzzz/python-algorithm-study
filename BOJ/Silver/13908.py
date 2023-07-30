import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) # 비밀번호의 길이 n, 비밀번호에 들어가는 수 m개
nums = []
if m != 0 : nums = list(map(int, input().rstrip().split()))

pw = [-1 for i in range(n)]
visited = [0 for i in range(10)]

ans = 0

def backtracking(pw, depth) :

    global ans

    if depth == n :
        flag = True

        for num in nums :
            if visited[num] == 0 :
                flag = False
                break

        if flag : ans += 1

        return

    for i in range(10) :
        pw[depth] = i
        visited[i] += 1

        backtracking(pw, depth + 1)

        visited[i] -= 1

backtracking(pw, 0)
print(ans)
