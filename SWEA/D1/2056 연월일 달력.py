t = int(input())

for i in range(t) :
    date = input()
    date = date[0:4] + '/' + date[4:6] + '/' + date[6:8]
    mm, dd = int(date[5:7]), int(date[8:])

    if (mm in [1, 3, 5, 7, 8, 10, 12] and 0 < dd < 32) | (mm == 2 and 0 < dd < 29) | (mm in [4, 6, 9, 11] and 0 < dd < 31) :
        print(f'#{i + 1} {date}')
    else :
        print(f'#{i + 1} -1')
