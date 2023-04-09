import sys
input = sys.stdin.readline

n = int(input())

ans = []

def backtracking(depth) :
    # base
    if depth == n :
        print(*ans)
        return

    # recursive
    else :
        for i in range(1, n + 1) :
            if i not in ans :
                ans.append(i)
                backtracking(depth + 1)
                ans.pop()

backtracking(0)
