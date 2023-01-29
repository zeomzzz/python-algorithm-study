# A * B * C 의 결과의 0 ~ 9의 개수를 리스트의 인덱스 사용하여 count 
A = int(input())
B = int(input())
C = int(input())
cnt_lst = [0] * 10 # 0 ~ 9 개수 세기 위한 리스트

num_lst = list(str(A * B * C)) # A * B * C 의 각 자리 수가 요소인 리스트

for i in num_lst :
    cnt_lst[int(i)] += 1

for i in cnt_lst :
    print(i)
