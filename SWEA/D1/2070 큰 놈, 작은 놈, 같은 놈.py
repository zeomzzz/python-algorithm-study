t = int(input())

for i in range(t) :
    x, y = map(int, input().split())

    if x < y : result = '<'
    elif x > y : result = '>'
    else : result = '='
    
    print(f'#{i+1} {result}')
