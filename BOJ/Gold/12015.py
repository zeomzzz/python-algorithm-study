import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))

maxLen = 0
lis = []

def search(target) :

    start = 0
    end = len(lis) - 1

    while start <= end :
        mid = (start + end) // 2

        if lis[mid] == target : return mid
        elif lis[mid] < target : start = mid + 1
        else : end = mid - 1

    return start

for a in A :
    if len(lis) > 0 :
        if lis[-1] < a : lis.append(a)
        else :
            idx = search(a)
            lis[idx] = a
    else :
        lis.append(a)

print(len(lis))
