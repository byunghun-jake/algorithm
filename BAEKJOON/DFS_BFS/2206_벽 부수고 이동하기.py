# 벽을 부술 수 있는 기회 1
# dq = [[r, c, punch]]
# 4 방향으로 탐색
# 벽을 만났을 때
    # 1. 벽을 부순다.
    # 2. 벽을 부수지 않는다.

# 방문기록을 할 때, 그 위치에 벽을 부수고 갈 기회가 있는상태에서 도착했는지 없는 상태에서 도착했는지 구분

from collections import deque
import sys


def bfs():
    while dq:
        cr, cc, punch = dq.popleft()

        if cr == R and cc == C:
            return visited[cr][cc][punch]

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if nr in range(N) and nc in range(M) and not visited[nr][nc][punch]:
                if MAP[nr][nc] == 1 and punch == 1:
                    dq.append((nr, nc, punch - 1))
                    visited[nr][nc][punch - 1] = visited[cr][cc][punch] + 1
                elif MAP[nr][nc] == 0:
                    dq.append((nr, nc, punch))
                    visited[nr][nc][punch] = visited[cr][cc][punch] + 1
    else:
        return -1


N, M = map(int, input().split())
R = N - 1
C = M - 1

MAP = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# r, c, punch
dq = deque([(0, 0, 1)])
visited[0][0][1] = 1

answer = bfs()

print(answer)

