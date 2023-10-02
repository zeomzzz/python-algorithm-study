# 1. 바꿀 수 있는 단어인지 확인 : 한 글자만 다른 단어인가?
# 2. 그 중에서 not visited 인거로 바꿔보기
# 3. 안되면 backtracking

def solution(begin, target, words):
    global visited, answer
    
    answer = len(words) + 1
    visited = [0] * len(words)
    
    if target not in words : return 0

    backtracking(begin, 0, target, words)
    
    return answer

def compare(word1, word2) :
    
    cnt = 0
    
    for i in range(len(word1)) :
        if word1[i] != word2[i] :
            cnt += 1
            
            if cnt == 2 : return False
    
    if cnt == 0 : return False
    
    return True

# cur : 지금 단어 상태, depth : 몇 단계
def backtracking(cur, depth, target, words) : 
    global visited, answer
    
    # base case
    if cur == target :
        answer = min(answer, depth) # min 업데이트
        return
    
    # recursive
    # 1. 방문 가능한 단어 찾기
    for idx in range(len(words)) :
        if visited[idx] == 0 and compare(cur, words[idx]) :
            visited[idx] = 1
            backtracking(words[idx], depth + 1, target, words)
            visited[idx] = 0 # 원복
            
