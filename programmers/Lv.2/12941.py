def solution(A, B):
    
    answer = 0
    
    A.sort()
    B.sort(reverse = True)
    
    for i in range(len(A)) :
        answer += A[i] * B[i]

    return answer

# 처음에 썼던 backtracking 코드 (시간초과로 런타임에러)
# def backtracking(idx, depth, result, A, B):
#     global visited, answer
#
#     if result >= answer: return
#
#     if idx == depth:
#         if result < answer: answer = result
#         return
#
#     for i in range(idx):
#         if visited[i] == 0:  # 아직 idx 번째는 방문 안했으면
#             result += A[depth] * B[i]
#             visited[i] = 1
#
#             backtracking(idx, depth + 1, result, A, B)
#
#             result -= A[depth] * B[i]
#             visited[i] = 0
