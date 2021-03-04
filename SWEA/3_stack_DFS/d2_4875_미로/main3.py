# 갈 수 없음 => 1
# 갈 수 있음 => 0
# 출발지점 => 2
# 도착지점 => 3
import sys

sys.stdin = open("input.txt")


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def dfs(sr, sc):
    visited = [[False] * N for _ in range(N)]
    stack = [(sr, sc, [(sr, sc)])]
    visited[sr][sc] = True

    while stack:
        cr, cc, route = stack.pop()
        for idx in range(4):
            r = cr + dr[idx]
            c = cc + dc[idx]
            if -1 < r < N and -1 < c < N:
                if maze[r][c] != 1 and not visited[r][c]:
                    temp_route = route[:]
                    temp_route.append((r, c))
                    stack.append((r, c, temp_route))
                    visited[r][c] = True
                    if maze[r][c] == 3:
                        # print(temp_route)
                        return 1
    else:
        return 0


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    # 시작지점 찾기
    s_node = None
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                s_node = (i, j)
                break
    result = dfs(s_node[0], s_node[1])
    print(f"#{tc} {result}")
