import sys, heapq
input = sys.stdin.readline

plus = []
minus = []

n = int(input())

for _ in range(n) :
    x = int(input())

    if x != 0 :
        if x > 0 :
            heapq.heappush(plus, x)
        else :
            heapq.heappush(minus, x * (-1))
    else :
        pl = len(plus)
        ml = len(minus)

        if pl == 0 and ml == 0 :
            print(0)
        elif pl == 0 and ml != 0 :
            print(heapq.heappop(minus) * (-1))
        elif pl != 0 and ml == 0 :
            print(heapq.heappop(plus))
        else :
            if minus[0] <= plus[0] :
                print(heapq.heappop(minus) * (-1))
            else :
                print(heapq.heappop(plus))
