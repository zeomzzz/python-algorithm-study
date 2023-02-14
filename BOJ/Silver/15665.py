'''
1) set 이용하여 Arr의 중복 제거
2)
2-1) M == 1 : [1], [2], ... [N]
2-2) else : solution(N, M-1) 각 요소에 Arr 각 요소를 추가
'''

def solution(N, M, Arr) :
  # set 이용하여 중복 제거
  arr = sorted(list(set(Arr)))
  ans = []

  if M == 1 :
    for i in arr :
      ans.append([i])
  else :
    for i in solution(N, M-1, Arr) :

      for j in arr :
        tmp_arr = i[:]
        tmp_arr.append(j)
        ans.append(tmp_arr)

  return ans

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in solution(n, m, arr) :
    i_tmp = list(map(str, i))
    print(' '.join(i_tmp))
