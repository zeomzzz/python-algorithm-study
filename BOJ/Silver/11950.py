n, m = map(int, input().split())

flag = []
for _ in range(n) :
  f = list(input()[:])
  flag.append(f)

min = n*m
for w in range(0, n-2) :
  for b in range(w+1, n-1) :
    
    cnt = 0

    for r in range(n):
      for c in range(m) :
        if r <= w :
          if flag[r][c] != 'W' :
            cnt += 1
        elif r <= b :
          if flag[r][c] != 'B' :
            cnt += 1
        else :
          if flag[r][c] != 'R' :
            cnt += 1
    
    if cnt < min :
      min = cnt

print(min)
