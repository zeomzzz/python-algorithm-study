h, m = map(int, input().split())

time = h * 60 + m - 45
h_new = time // 60
m_new = time % 60

if h_new < 0 : print(h_new + 24, m_new)
else : print(h_new, m_new)
