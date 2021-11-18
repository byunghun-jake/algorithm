dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def dfs(sr, sc):
    visited = [[False] * (N + 1) for _ in range(N + 1)]
    stack = [[sr, sc]]
    visited[sr][sc] = True

    while stack:
        cr, cc = stack[-1]
        for di in range(4):
            nr = cr + dr[di]
            nc = cc + dc[di]
            if nr < 0 or N <= nr or nc < 0 or N <= nc:
                continue
            if visited[nr][nc]:
                continue
            if maze[nr][nc] == 1:
                continue
            if maze[nr][nc] == 3:
                return 1
            if maze[nr][nc] == 0:
                stack.append([nr, nc])
                visited[nr][nc] = True
                break
        else:
            stack.pop()
    else:
        return 0


T = int(input())

for _ in range(T):
    # N: 미로의 크기
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    sr, sc = 0, 0
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                sr = r
                sc = c
                break

    answer = dfs(sr, sc)
    print(answer)
