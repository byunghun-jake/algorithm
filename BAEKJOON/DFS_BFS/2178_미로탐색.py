# 1 은 이동할 수 있는 칸
    # 갈 수 있는지 없는지 확인
    # 방문했는지 하지 않았는지 확인

# 지나야 하는 최소의 칸 수를 출력한다.
    # 최소 칸을 알기 위해서는 bfs를 사용한다.

# N: 행의 크기
# M: 열의 크기

from collections import deque

N, M = map(int, input().split())

MAP = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    dq = deque([(sr, sc, 1)])
    visited[sr][sc] = True

    while dq:
        cr, cc, count = dq.popleft()

        for di in range(4):
            nr = cr + dr[di]
            nc = cc + dc[di]

            if nr in range(N) and nc in range(M) and MAP[nr][nc] and not visited[nr][nc]:
                if nr == N - 1 and nc == M - 1:
                    print(count + 1)
                    return

                dq.append((nr, nc, count + 1))
                visited[nr][nc] = True

bfs(0, 0)
