import sys
input = sys.stdin.readline


lst = [1] * 1000001
for i in range(2, 1000001) :
    if lst[i]:
        tmp = 2
        while True:
            idx = i * tmp

            if idx > 1000000 : break

            lst[idx] = 0
            tmp += 1

while True :

    N = int(input().rstrip())

    if N == 0 : break

    for a in range(3, N, 2) :

        b = N - a

        if b < a:
            print("Goldbach's conjecture is wrong.")
            break

        if lst[a] : # a가 소수이면

            if lst[b] :
                print(str(N) + " = " + str(a) + " + " + str(b))
                break
