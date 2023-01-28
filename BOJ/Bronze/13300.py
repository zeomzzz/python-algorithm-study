N, K = map(int, input().split()) # 전체 학생 수 N, 방 별 최대 인원 수 K

num_lst = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

room_num = 0

for t in range(N) :
  r, c = map(int, input().split())

  num_lst[r][c-1] += 1

for r in range(2) :
  for c in range(6) :
    
    if num_lst[r][c] != 0 :
      room_num += num_lst[r][c] // K

      if num_lst[r][c] % K > 0 :
        room_num += 1

print(room_num)
