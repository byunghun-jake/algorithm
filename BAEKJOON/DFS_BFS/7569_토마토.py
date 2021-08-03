# 3차원 행렬
#   MAP = [
#       [
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0],
#           [0, 0, 0, 0, 0]
#       ],
#       [
#           [0, 0, 0, 0, 0],
#           [0, 0, 1, 0, 0],
#           [0, 0, 0, 0, 0]
#       ]
#   ]
from collections import deque
from sys import stdin

dh = [-1, 1, 0, 0, 0, 0]
dr = [0, 0, -1, 0, 1, 0]
dc = [0, 0, 0, 1, 0, -1]

def bfs():
    global change_tomato, early_tomato
    while dq:
        ch, cr, cc, day = dq.popleft()

        for i in range(6):
            nh = ch + dh[i]
            nr = cr + dr[i]
            nc = cc + dc[i]
            if nh in range(H) and nr in range(R) and nc in range(C) and MAP[nh][nr][nc] == 0:
                dq.append((nh, nr, nc, day + 1))
                MAP[nh][nr][nc] = 1
                early_tomato -= 1
                if early_tomato == 0:
                    return day + 1
    return -1


C, R, H = map(int, input().split())

MAP = []

dq = deque([])
early_tomato = 0
change_tomato = 0

for h in range(H):
    floor = []
    for r in range(R):
        row = list(map(int, stdin.readline().strip().split()))
        for c in range(C):
            # 익지 않았다면, 개수를 센다.
            if row[c] == 0:
                early_tomato += 1
            # 익었다면, 위치를 저장한다.
            elif row[c] == 1:
                dq.append((h, r, c, 0))
        floor.append(row)
    MAP.append(floor)

# 익은 토마토를 기준으로 탐색을 시작한다.
# BFS로 탐색한다.
if early_tomato == 0:
    print(0)
else:
    print(bfs())

