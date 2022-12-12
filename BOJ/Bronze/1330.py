x, y = map(int, input().split())
# split 아무것도 입력 안하면 공백 기준 split
# map 이용해서 x, y를 int로 변환

if x > y : print('>')
elif x < y : print('<')
else : print('==')
