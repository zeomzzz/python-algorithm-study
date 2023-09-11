from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    q = deque()
    
    for i in range(bridge_length) : q.append(0)
    
    weight_sum = 0
    idx = 0 # truck_weights의 인덱스
    truck_num = len(truck_weights)
    pass_cnt = 0 # 트럭 몇 대가 다리를 완전히 지났는지
    
    while q :
        
        # 트럭이 한 칸 씩 앞으로
        truck_passed = q.popleft()
        weight_sum -= truck_passed
        if truck_passed : pass_cnt += 1 # 나온 트럭 +1
        
        # 다음 트럭 올라갈 수 있으면 올리기
        if idx < truck_num and weight_sum + truck_weights[idx] <= weight :
            q.append(truck_weights[idx]) # 트럭 올리고
            weight_sum += truck_weights[idx] # 무게 갱신
            idx += 1 # 다음 트럭 ㄱㄱ
        else : q.append(0) # 트럭 못 올리는 경우
        
        answer += 1
        
        if pass_cnt == truck_num : break
    
    return answer
