while True :
    tri = list(map(int, input().split()))
    tri.sort(reverse = True)

    if tri == [0, 0, 0] :
        break
    else :
        if tri[0] ** 2 == tri[1] ** 2 + tri[2] ** 2 :
            print('right')
        else :
            print('wrong')
