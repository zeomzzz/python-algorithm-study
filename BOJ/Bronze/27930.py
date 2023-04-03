import sys
input = sys.stdin.readline

s_lst = list(input().rstrip())

korea = ["K", "O", "R", "E", "A"]
yonsei = ["Y", "O", "N", "S", "E", "I"]

isK = [] # KOREA 확인
isY = [] # YONSEI 확인

k = 0
y = 0

for s in s_lst :
    if s == korea[k] :
        isK.append(s)
        k += 1

        if len(isK) == len(korea) :
            print("KOREA")
            break

    if s == yonsei[y] :
        isY.append(s)
        y += 1

        if len(isY) == len(yonsei) :
            print("YONSEI")
            break
