n = int(input())

max_cnt = 0
max_n = 0

for i in range(1, n) :
    cnt = 2
    pattern = [n, n - i]

    while True :
        num = pattern[-2] - pattern[-1] # 새로 추가할 수
        if num >= 0 :
            cnt += 1
            pattern.append(num)
        else :
            break

    if cnt > max_cnt :
        max_cnt = cnt
        max_n = i

pattern = [n, n - max_n]
while True :
    num = pattern[-2] - pattern[-1]
    if num >= 0 : pattern.append(num)
    else : break

print(len(pattern))
print(*pattern)
