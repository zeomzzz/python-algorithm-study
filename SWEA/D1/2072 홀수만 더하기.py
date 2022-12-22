t = int(input())

for i in range(t) :
    sum = 0
    nums = list(map(int, input().split()))

    for j in nums :
        if j % 2 == 1 :
            sum += j

    print('#' + str(i+1) + ' ' + str(sum))
