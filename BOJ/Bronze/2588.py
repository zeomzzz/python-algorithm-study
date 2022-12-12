A, B = int(input()), int(input())
# input이 줄바꿈으로 주어질 때는 input(), input()

print(A * (B % 10)) #(3)
print(A * ((B % 100) - (B % 10))//10) #(4)
print(A * (B // 100)) #(5)
print(A * B) #(6)
