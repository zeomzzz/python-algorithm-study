import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, s = map(int, input().split()) # 정수 n개, 합 s
lst = list(map(int, input().split())) # 정수 n개
lst.sort()
boolLst = [False] * n
cnt = 0

def findSum(idx, curSum) :

    global cnt

    # 기저조건
    if idx == n :
        if curSum == s :
            cnt += 1
        return

    # 유도조건
    boolLst[idx] = True
    findSum(idx + 1, curSum + lst[idx])

    boolLst[idx] = False
    findSum(idx + 1, curSum)

findSum(0, 0)

# 부분집합이 공집합인 경우(부분 수열의 크기가 양수가 아님) sum이 0 -> -1 해줘야 함
if s == 0 : cnt -= 1

print(cnt)
