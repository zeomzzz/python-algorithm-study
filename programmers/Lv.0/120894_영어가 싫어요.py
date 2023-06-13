# 두 번째 풀이 : replace 이용

def solution(numbers):
    answer = 0
    
    num_replaced = numbers.replace('zero', '0')
    num_replaced = num_replaced.replace('one', '1')
    num_replaced = num_replaced.replace('two', '2')
    num_replaced = num_replaced.replace('three', '3')
    num_replaced = num_replaced.replace('four', '4')
    num_replaced = num_replaced.replace('five', '5')
    num_replaced = num_replaced.replace('six', '6')
    num_replaced = num_replaced.replace('seven', '7')
    num_replaced = num_replaced.replace('eight', '8')
    num_replaced = num_replaced.replace('nine', '9')
    
    answer = int(num_replaced)
    
    return answer


# 첫 풀이 : slicing 이용하여 비교

def solution(numbers):
    answer = 0
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_thr = ["zer", "one", "two", "thr", "fou", "fiv", "six", "sev", "eig", "nin"]
    tmp_list = []
    start = 0
    
    while True :
        tmp_num = numbers[start : start + 3]
        for i in num_thr :
            if tmp_num == i :
                tmp_list.append(num_thr.index(i))
                start += len(num_list[num_thr.index(i)])
        if start == len(numbers) :
            break
    
    for j in range(len(tmp_list)) :
        answer += tmp_list[j] * (10 ** (len(tmp_list) - (j + 1)))
            
    return answer
