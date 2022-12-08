# 풀이 1. 폰켓몬 종류 수, 뽑아야 하는 개수 중 작은 값

def solution(nums):
    
    n = len(nums) // 2
    p_cnt = len(set(nums))
    
    return min(n, p_cnt)
