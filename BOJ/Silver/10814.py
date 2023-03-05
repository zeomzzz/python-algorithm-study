n = int(input()) # 회원 수

members = [[] for _ in range(201)]  # 나이 1 ~ 200

for _ in range(n) :
    age, name = input().split()
    age = int(age)

    members[age].append(name)

for i in range(201) :
    if len(members[i]) > 0 :
        for k in members[i] :
            print(str(i) + " " + k)
