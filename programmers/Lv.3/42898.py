def solution(m, n, puddles):
    
    map = [([0] + [-1] * m) for _ in range(n)]
    map.insert(0, [0] * (m + 1))
    
    for puddle in puddles : map[puddle[1]][puddle[0]] = 0
    
    map[1][1] = 1
    
    for c in range(1, m + 1) :
        for r in range(1, n + 1) :
            if map[r][c] == -1 : # 아직 지나가지 않음
                map[r][c] = (map[r-1][c] + map[r][c-1]) % 1000000007
    
    return map[n][m] if map[n][m] != -1 else 0
