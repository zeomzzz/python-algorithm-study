import sys
input = sys.stdin.readline

def backtracking(idx, depth) :
    # base
    if depth == 6 :
        print(*ans)
        return

    # recursive
    else :
        for i in range(idx, k) :
            ans.append(S[i])
            backtracking(i+1, depth + 1)
            ans.pop()


while True :
    S = list(map(int, input().split()))
    if S == [0] : break

    k = S[0]
    del S[0]

    ans = []

    backtracking(0, 0)
    print()
