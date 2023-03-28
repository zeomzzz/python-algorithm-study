import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

def possible(idx) :
    for i in range(idx) : # 지금까지 둔 위치들이랑 비교(idx 전)
        if sel[idx] == sel[i] or idx - i == abs(sel[idx] - sel[i]) : # 같은 위치에 또 뒀거나 대각선에 있으면
            return False
    return True

def nqueen(idx) :
    global ans, sel

    # base
    if idx == n :
        ans += 1
        return

    # recursive
    for i in range(n) :
        sel[idx] = i # idx 번째 위치에 i를 놓아봄
        if possible(idx) : # 그런데 이 위치(idx)에 둬도 되나?
            nqueen(idx + 1) # idx+1 번째 자리에 두러 감 (안되면 idx에 다른거 넣어봄)

n = int(input())
sel = [0] * n
ans = 0

nqueen(0)

print(ans)
