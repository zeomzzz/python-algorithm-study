import sys

n = int(sys.stdin.readline().rstrip())

lst = [0] * 11 # index 1 ~ 10 사용
lst[1] = 1
lst[2] = 2
lst[3] = 4

def find_sum(x) :
    if lst[x] != 0 :
        return lst[x]
    else :
        lst[x] = find_sum(x - 1) + find_sum(x - 2) + find_sum(x - 3)
        return lst[x]

for _ in range(n) :
    print(find_sum(int(sys.stdin.readline().rstrip())))
