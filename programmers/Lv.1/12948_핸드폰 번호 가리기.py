def solution(phone_number):
    answer = ''
    num_replace = len(phone_number) - 4
    
    answer = '*' * num_replace + str(phone_number[num_replace:len(phone_number)])
    
    return answer
