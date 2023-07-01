import sys
input = sys.stdin.readline

N = int(input().rstrip())

nums = [1 for _ in range(N + 1)] # 소수는 1로 표시
nums[0] = nums[1] = 0

for i in range(2, N + 1) :
    a = 2

    while i * a <= N :
        if nums[i * a] == 1 : nums[i * a] = 0
        a += 1

primes = []

for i in range(1, N + 1) :
    if nums[i] == 1 : primes.append(i)

start = 0
end = 0

cnt = 0
if len(primes) > 0 : nsum = primes[start]

l = len(primes)

while end < l and len(primes) > 0 :

    if nsum == N : # N이다!
        cnt += 1 # 하나 찾음

    if nsum < N :
        end += 1
        if end < l : nsum += primes[end]
    elif nsum >= N :
        start += 1
        end = start

        if start < l : nsum = primes[start]

print(cnt)
