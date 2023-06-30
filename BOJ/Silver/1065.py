import sys
input = sys.stdin.readline

N = int(input().rstrip())

cnt = 0

for num in range(1, N + 1) :
    if num < 100 :
        cnt += 1
    else : # num은 999 이하
        tmp = str(num)
        if int(tmp[2]) - int(tmp[1]) == int(tmp[1]) - int(tmp[0]) :
            cnt += 1

print(cnt)
