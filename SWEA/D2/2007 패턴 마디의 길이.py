T = int(input())

for _ in range(T) :
    str = input()
    for i in range(len(str)) :
        if str[:i + 1] == str[i + 1 : 2 * i + 2] :
            print(f'#{_ + 1} {i + 1}')
            break
