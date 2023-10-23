def solution(name):
    global l, letters, visited, answer, cnt
    
    answer = 20 * 26 + 1
    
    l = len(name)
    visited = [0] * l
    letters = [0] * l
    cnt = 0
    for i in range(l) :
        if name[i] == 'A' : 
            visited[i] = 1
            cnt += 1
        else  : letters[i] = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
    
    backtracking(0, 0)
    
    return answer

def backtracking(idx, cnt_sum) :
    global l, letters, visited, answer, cnt
    
    if cnt == l :
        answer = min(cnt_sum, answer)
        return
    
    for i in range(l // 2 + 1) :
        tmp_idx = idx - i
        while tmp_idx < 0 : tmp_idx += l
        if visited[tmp_idx] == 0 and cnt_sum + letters[tmp_idx] <= answer :
            visited[tmp_idx] = 1
            cnt += 1
            backtracking(tmp_idx, cnt_sum + letters[tmp_idx] + i)
            visited[tmp_idx] = 0
            cnt -= 1
        
        tmp_idx = idx + i
        while tmp_idx >= l : tmp_idx -= l
        if i != 0 and not visited[tmp_idx] and cnt_sum + letters[tmp_idx] <= answer :
            visited[tmp_idx] = 1
            cnt += 1
            backtracking(tmp_idx, cnt_sum + letters[tmp_idx] + i)
            visited[tmp_idx] = 0
            cnt -= 1
