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
        if len(tmp_arr) > 0 and j >= tmp_arr[-1] :
          tmp_arr.append(j)
          ans.append(tmp_arr)

  return ans

n, m = map(int, input().split())
arr = list(map(int, input().split()))

for i in solution(n, m, arr) :
    i_tmp = list(map(str, i))
    print(' '.join(i_tmp))
