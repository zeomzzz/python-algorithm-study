h, m = map(int, input().split())
t = int(input())

time = h * 60 + m + t

h_new = time // 60
if h_new > 23 : h_new -= 24

m_new = time % 60

print(h_new, m_new)
