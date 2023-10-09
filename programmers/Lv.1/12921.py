def solution(n):
    answer = 0
    
    nums = [1] * (n + 1)
    nums[0] = 0
    nums[1] = 0
    
    for i in range(2, n) :
        if nums[i] == 1 :
            for j in range(2 * i, n + 1, i) :
                nums[j] = 0
    
    return sum(nums)
