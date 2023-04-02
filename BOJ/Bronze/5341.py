import sys
input = sys.stdin.readline

while True :
    x = int(input())
    ans = 0

    if x == 0 : break

    else :
        for i in range(1, x + 1) :
            ans += i
        print(ans)
