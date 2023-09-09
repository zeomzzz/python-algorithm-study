def solution(today, terms, privacies):
    answer = []
    
    # 1. 
    today_yr, today_mth, today_dt = map(int, today.split("."))
    today_days = today_yr * 12 * 28 + today_mth * 28 + today_dt
    
    # 2. 
    terms_dic = {}
    for term in terms :
        type, months = term.split(" ")
        terms_dic[type] = int(months)
    
    # 3. 
    idx = 1
    for privacy in privacies :
        start, type = privacy.split(" ")
        start_yr, start_mth, start_dt = map(int, start.split("."))
        start_days = start_yr * 12 * 28 + start_mth * 28 + start_dt
        
        # 유효기간 구하기
        end_days = start_days + terms_dic[type] * 28 - 1
        
        if today_days > end_days :
            answer.append(idx)
        
        idx += 1
        
    return answer
