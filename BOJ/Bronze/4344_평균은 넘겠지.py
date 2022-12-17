c = int(input())

for i in range(c) :
    lst = list(map(int, input().split()))
    avg = sum(lst[1:]) / lst[0]
    cnt = 0

    for j in lst[1:] :
        if j > avg :
            cnt += 1
    
    rate = cnt * 100 / lst[0]

    print(f'{rate:.3f}%')
