# 풀이 1 : 이중 for문으로 string[n]이 담긴 리스트와 string의 string[n] 비교

def solution(strings, n):
    answer = []
    
    n_str = list(i[n] for i in strings)
    n_str.sort()
    
    strings.sort()
    
    for j in n_str :
        for k in strings :
            if j == k[n] :
                answer.append(k)
                strings.remove(k)
                break
    
    return answer
  
  
# 풀이 2 : sorted key, lambda 이용
  
def solution(strings, n):
    
    strings.sort()
    answer = sorted(strings, key = lambda x : x[n])
    
    return answer
