# 풀이 1

def solution(s):
    
    lst = [int(i) for i in s.split(' ')]
    
    return str(min(lst)) + ' ' + str(max(lst))


# 풀이 2 : map 이용
 
def solution(s):
    
  lst = list(map(int, s.split(' ')))
    
  return str(min(lst)) + ' ' + str(max(lst))
