import sys
input = sys.stdin.readline

S = input().rstrip()

if len(S) == 0 :
    print("NO")
else :
    S = S.replace("pi", " ")
    S = S.replace("ka", " ")
    S = S.replace("chu", " ")

    if len(S.rstrip()) == 0 : print("YES")
    else : print("NO")
