import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def dfs(cur) :
    global ans

    isTeam[cur] = 1
    team.append(cur)
    nxt = students[cur]

    if isTeam[nxt] :
        if nxt in team :
            ans += team[team.index(nxt) : ]
        return
    else :
        dfs(nxt)

T = int(input().rstrip())

for _ in range(T) :
    n = int(input())
    students = list(map(int, input().rstrip().split()))
    students.insert(0, 0)
    isTeam = [0 for _ in range(n + 1)]
    ans = []

    for i in range(1, n + 1) :
        if not isTeam[i] :
            team = []
            dfs(i)

    print(n - len(ans))
