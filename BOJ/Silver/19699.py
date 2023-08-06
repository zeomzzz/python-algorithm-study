import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M = map(int, input().rstrip().split()) # N마리 소 중 M마리 소
Hs = list(map(int, input().rstrip().split()))

# 가능한 몸무게의 합 모두 구하고
# 소수가 아닌 건 빼기

ans = []

def isPrime(num) :
    ans = True
    if num == 1 : ans = False
    elif num > 2 :
        for i in range(2, num) :
            if num % i == 0 :
                ans = False
                break
    return ans

def backtracking(idx, depth, hsum) :

    # base
    if depth == M :
        if isPrime(hsum) : ans.append(hsum)
        return

    # recursive
    for i in range(idx, N) :
        hsum += Hs[i]
        backtracking(i + 1, depth + 1, hsum)
        hsum -= Hs[i]

backtracking(0, 0, 0)

ans = list(set(ans))
ans.sort()

if len(ans) : print(*ans)
else : print(-1)
