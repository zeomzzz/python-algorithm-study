# 풀이 1. n을 3으로 나눈 나머지 lst에 추가하여 10진수로 변환
def solution(n):
    answer = 0
    tri_lst = []
    n_reversed = 0
    
    while n > 0 :
        tri_lst.append(n % 3)
        n = n // 3
    
    m = len(tri_lst) - 1
    for i in tri_lst :
        n_reversed += i * (3 ** m)
        m -= 1
        
    return n_reversed
  
  
  # 풀이 2. int(n, m)이 m진수인 str n을 10진수로 변환함을 이용
  def solution(n):
    tmp = ''
    
    while n > 0 :
        tmp += str(n % 3)
        n = n // 3
    
    answer = int(tmp, 3)
    
    return answer
