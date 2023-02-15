N = int(input())
N_arr = list(map(int, input().split())) # A[1], A[2], A[3], ..., A[N]
M = int(input())
M_arr = list(map(int, input().split())) # key

# 1) N_arr을 정렬
N_arr.sort()

# 2) 이진검색으로 M_arr의 요소 검색
for tc in range(M) :
  key = M_arr[tc]
  isArr = False

  start = 0
  end = N-1

  while start <= end :
    mid = int((start + end) / 2)

    if N_arr[mid] == key :
      isArr = True
      break
    elif N_arr[mid] > key :
      end = mid - 1
    else :
      start = mid + 1
    
  if isArr :
    print(1)
  else :
    print(0)
