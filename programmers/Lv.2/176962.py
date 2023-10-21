def solution(plans):
    answer = []
    stack = []
    stop_stack = []
    
    # stack에 필요한 자료형으로 넣어주고 시작 시간에 따라 오름차순 정렬
    for name, start, playtime in plans :
        start_time = int(start[:2]) * 60 + int(start[3:])
        stack.append([start_time, name, int(playtime)])
    stack.sort()
    
    # 가보자고..
    cur_time, cur_name, cur_playtime = stack.pop(0)
    while stack :
        nxt_time, nxt_name, nxt_playtime = stack.pop(0)
        if cur_time + cur_playtime == nxt_time : # 과제를 끝낸 시간에 새로 시작해야하는 과제가 있음
            answer.append(cur_name)
            cur_time, cur_name, cur_playtime = nxt_time, nxt_name, nxt_playtime
        elif cur_time + cur_playtime < nxt_time : # 진행 중인 과제를 끝냄
            answer.append(cur_name)
            if stop_stack : # 그런데 멈춘게 있음
                stack.insert(0, [nxt_time, nxt_name, nxt_playtime]) # 꺼낸거 다시 넣고
                cur_time = cur_time + cur_playtime # 다음엔 멈춘거 중에 고..
                cur_name, cur_playtime = stop_stack.pop(0)
            else : # 멈춘거 없음
                cur_time, cur_name, cur_playtime = nxt_time, nxt_name, nxt_playtime
        else : # 진행중인게 더 큼
            # stop 스택에 넣기
            stop_stack.insert(0, [cur_name, cur_playtime - (nxt_time - cur_time)])
            cur_time, cur_name, cur_playtime = nxt_time, nxt_name, nxt_playtime
    
    answer.append(cur_name)
    
    while stop_stack : answer.append(stop_stack.pop(0)[0])
    
    return answer
