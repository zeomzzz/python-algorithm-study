import sys, heapq
input = sys.stdin.readline

n = int(input())
leftheap = [] # 최대힙
rightheap = [] # 최소힙
# rightheap[0]이 중간값이 되도록 입력하기 !!

for i in range(n) :
    x = int(input())

    if i == 0 :
        heapq.heappush(rightheap, x)
    else :
        if x < rightheap[0] :
            heapq.heappush(leftheap, x * (-1))
        else :
            heapq.heappush(rightheap, x)

        # push 하고 갯수 맞춰줘야함
        # rightheap이  한개 또는 두개 많도록
        if len(rightheap) <= len(leftheap) :
            tmp = heapq.heappop(leftheap) * (-1)
            heapq.heappush(rightheap, tmp)
        elif len(rightheap) - len(leftheap) > 2 :
            tmp = heapq.heappop(rightheap) * (-1)
            heapq.heappush(leftheap, tmp)

    print(rightheap[0])
