# 첫 풀이

def solution(n, arr1, arr2):
    answer = []
    wid = len(arr1)
    
    bin1 = [int(bin(i)[2:]) for i in arr1]
    bin2 = [int(bin(j)[2:]) for j in arr2]
    
    bin_sum = [str(x + y) for x, y in zip(bin1, bin2)]
    
    for k in range(wid) :
        while len(bin_sum[k]) < wid :
            bin_sum[k] = "0" + bin_sum[k]
    
    for l in bin_sum :
        solved = ''
        for m in l :
            if int(m) > 0 :
                solved += "#"
            else :
                solved += " "
        answer.append(solved)
    
    return answer

  
# 풀이 2. zfill 이용

def solution(n, arr1, arr2):
    answer = []
    
    bin1 = [int(bin(i)[2:]) for i in arr1]
    bin2 = [int(bin(j)[2:]) for j in arr2]
    
    bin_sum = [str(x + y).zfill(n) for x, y in zip(bin1, bin2)]
    
    for k in bin_sum :
        solved = k
        solved = solved.replace("0", " ")
        solved = solved.replace("1", "#")
        solved = solved.replace("2", "#")
        answer.append(solved)

    return answer
 

# 풀이 3. 비트연산자 사용

def solution(n, arr1, arr2):
    answer = []
    
    for i, j in zip(arr1, arr2) :
        solved = bin(i|j)[2:].zfill(n)
        solved = solved.replace("0", " ")
        solved = solved.replace("1", "#")
        answer.append(solved)

    return answer
