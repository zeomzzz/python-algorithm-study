import sys
input = sys.stdin.readline

n = int(input().rstrip())  # 점의 개수 n
dots = list(map(int, input().rstrip().split()))
dots.sort()

notodd = -1
odd = -1

for i in range(n - 1) :
    cnt = 0
    for j in range(i + 1, n) :
        d = abs(dots[i] - dots[j])

        if d % 2 == 0 :
            if notodd == -1 : notodd = d
            else :
                if d < notodd : notodd = d
                else : cnt += 1
        elif d % 2 == 1 :
            if odd == -1 : odd = d
            else :
                if d < odd : odd = d
                else : cnt += 1
        if cnt == 2 : break

print(str(notodd) + " " + str(odd))
