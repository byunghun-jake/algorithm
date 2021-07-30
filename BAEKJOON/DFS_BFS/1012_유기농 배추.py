# 지렁이의 이동 범위는 기준 위치에서 상하좌우
# 배추를 지키기 위해 필요한 최소 지렁이의 마리수를 구해라
# 배추 군집의 개수를 구하면 된다.

import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    dq = deque([(sr, sc)])
    visited[sr][sc] = 1

    while dq:
        cr, cc = dq.popleft()

        for di in range(4):
            nr = cr + dr[di]
            nc = cc + dc[di]
            if nr in range(N) and nc in range(M):
                if MAP[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    dq.append((nr, nc))


# T: 테스트 케이스
T = int(input())

for tc in range(T):
    # M: 가로 길이 (~50)
    # N: 세로 길이 (~50)
    # K: 배추의 개수 (~2500)
    M, N, K = map(int, input().split())

    answer = 0

    MAP = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        c, r = map(int, sys.stdin.readline().strip().split())
        MAP[r][c] = 1

    for r in range(N):
        for c in range(M):
            if MAP[r][c] and not visited[r][c]:
                bfs(r, c)
                answer += 1

    print(answer)


