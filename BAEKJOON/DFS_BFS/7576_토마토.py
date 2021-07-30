# 익은 토마토를 모두 찾아 dq에 담는다.
# (r, c, day)
# 순서대로 탐색을 시작한다.
# 모든 탐색이 끝난 뒤에 0인 값을 가지고 있는 위치가 있는지 확인한다.
from collections import deque


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs():
    global change_tomato
    result = 0
    while dq:
        cr, cc, day = dq.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if nr in range(R) and nc in range(C) and MAP[nr][nc] == 0:
                dq.append((nr, nc, day + 1))
                MAP[nr][nc] = 1
                result = day + 1
                change_tomato += 1

    return result



C, R = map(int, input().split())

MAP = [list(map(int, input().split())) for _ in range(R)]
# 직접 값을 바꿔보자

dq = deque([])

early_tomato = 0
change_tomato = 0
for r in range(R):
    for c in range(C):
        if MAP[r][c] == 1:
            dq.append((r, c, 0))
        elif MAP[r][c] == 0:
            early_tomato += 1


answer = bfs()

if early_tomato > change_tomato:
    answer = -1

print(answer)