# 풀이1. 대소문자 판별 -> 변경
def solution(my_string):
    answer = ''
    for i in my_string :
        if i.isupper() :
            answer += i.lower()
        else :
            answer += i.upper()
    return answer

# 풀이2. swapcase 함수 사용
def solution(my_string):
    answer = my_string.swapcase()
    return answer
