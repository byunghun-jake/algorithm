# 최소 몇 개의 칸을 지나면 도달할 수 있을까?
# 최소 => BFS

from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    dq = deque([[sr, sc, 0]])
    visited = [[False] * N for _ in range(N)]
    visited[sr][sc] = True

    while dq:
        cr, cc, count = dq.popleft()
        for di in range(4):
            nr = cr + dr[di]
            nc = cc + dc[di]
            if nr < 0 or N <= nr or nc < 0 or N <= nc:
                continue
            if visited[nr][nc] or maze[nr][nc] == 1:
                continue
            if maze[nr][nc] == 3:
                return count
            dq.append([nr, nc, count + 1])
            visited[nr][nc] = True
    return 0

T = int(input())

for _ in range(T):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    sr, sc = 0, 0
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr = r
                sc = c

    answer = bfs(sr, sc)
    print(answer)