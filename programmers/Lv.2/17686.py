def solution(files):
    answer = []
    results = []
    file_idx = 0
    
    for file in files :    
        idx = 0
        head, number, origin = "", 0, file
        
        while True :
            if ord(file[idx]) < ord("0") or ord(file[idx]) > ord("9") :
                head += file[idx]
                idx += 1
            else : break # number임
            
            if idx == len(file) : break # index out of range
        
        head = head.lower()
            
        cnt = 0
        while cnt < 5 :
            if idx == len(file) : break
            else :
                if ord("0") <= ord(file[idx]) <= ord("9") :
                    if number == "" and file[idx] == "0" : pass
                    else :
                        number = number * 10 + int(file[idx])
                    cnt += 1
                    idx += 1
                else : break
        
        results.append([head, number, file_idx, origin])
        
        file_idx += 1
        
    results.sort()
    
    for result in results : answer.append(result[-1])
        
    return answer
