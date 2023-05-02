import sys
input = sys.stdin.readline

for _ in range(3) :
    lst = list(map(int, input().rstrip().split()))
    a = sum(lst)

    if a == 3 : print("A")
    elif a == 2 : print("B")
    elif a == 1 : print("C")
    elif a == 0 : print("D")
    else : print("E")
