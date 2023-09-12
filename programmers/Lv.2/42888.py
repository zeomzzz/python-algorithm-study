# 닉네임 정보를 dictionary에 user id를 key로 저장
# 1. 최종 닉네임을 파악
# 2. record에 따라 answer
def solution(record):
    answer = []
    nickname_dic = {}
    for r in record :
        tmp_list = r.split(" ")
        
        if len(tmp_list) == 3 : 
            msg, uid, nickname = tmp_list[0], tmp_list[1], tmp_list[2]
            nickname_dic[uid] = nickname
    
    for r in record :
        tmp_list = r.split(" ")
        
        if len(tmp_list) == 3 : 
            msg, uid, nickname = tmp_list[0], tmp_list[1], tmp_list[2]
            if msg == "Enter" :
                tmp = nickname_dic[uid] + "님이 들어왔습니다."
                answer.append(tmp)
        else :
            msg, uid = tmp_list[0], tmp_list[1]
            tmp = nickname_dic[uid] + "님이 나갔습니다."
            answer.append(tmp)
        
    return answer
