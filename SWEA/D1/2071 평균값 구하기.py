t = int(input())

for i in range(t) :
    nums = list(map(int, input().split()))
    avg = round(sum(nums) / len(nums))

    print(f'#{i+1} {avg}')
