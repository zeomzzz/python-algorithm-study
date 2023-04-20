import sys
input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
seq = list(map(int, input().rstrip().split()))

for i in range(1, N) :
    seq[i] += seq[i - 1]

seq.insert(0, 0)

# 투포인터

left = 0
right = 1
minn = 1e9

while True :
    if seq[right] - seq[left] >= S :
        minn = min(minn, right - left)
        if left + 1 < N + 1 : left += 1
        else : break
    elif seq[right] - seq[left] < S :
        if right + 1 < N + 1: right += 1
        else : break

    if right <= left - 1 : break

if minn == 1e9 : minn = 0

print(minn)
