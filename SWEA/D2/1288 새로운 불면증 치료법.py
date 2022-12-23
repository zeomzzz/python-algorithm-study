T = int(input())

for i in range(T) :
    N = int(input())
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    j = 1

    while True :
        for k in str(j * N) :
            if k in nums :
                nums.remove(k)
        j += 1

        if nums == [] :
            print(f'#{i + 1} {(j - 1 ) * N}')
            break
