# 풀이 1 : list index 이용

def solution(s):
    
    num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    word = ["zero", "one", "two","three", "four", "five", "six", "seven", "eight", "nine"]
    
    for i in range(10) :
        s = s.replace(word[i], num[i])
    
    return int(s)
  

  # 풀이 2 : dict 입력하여 items 이용
  
  def solution(s):
    
    answer = s
    
    num_dict = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four", "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}
    
    for key, value in num_dict.items() :
        answer = answer.replace(value, key)
    
    return int(answer)
