# 풀이 1

def solution(number):
    answer = 0
    n = len(number)
    
    for i in range(0, n) :
        for j in range(i + 1, n) :
            for k in range(j + 1, n) :
                if i < j and j < k and number[i] + number[j] + number[k] == 0 :
                    answer += 1
                    
    return answer


# 풀이 2 : combinations 이용

from itertools import combinations

def solution(number):
    answer = 0
    
    for i in list(map(sum, combinations(number, 3))) :
        if i == 0 :
            answer += 1
    
    return answer
