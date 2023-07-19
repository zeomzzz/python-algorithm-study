import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
dolls = list(map(int, input().rstrip().split()))
lions = []

for i in range(N) : 
    if dolls[i] == 1 : lions.append(i)

ans = sys.maxsize

if len(lions) < K : ans = -1
else :
    start = 0
    end = K - 1

    ans = lions[end] - lions[start] + 1

    while True :
        start += 1
        end += 1

        if end < len(lions) : ans = min(ans, lions[end] - lions[start] + 1)
        else : break

print(ans)
