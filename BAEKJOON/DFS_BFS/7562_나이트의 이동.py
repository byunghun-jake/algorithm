# BFS
# 1. 8개 방향으로 이동
# 2. 방문 기록
# 3. queue 에 저장
# 몇 번만에 이동했는지 출력해야 한다.
from collections import deque

dr = [-2, -1, 1, 2, 2, 1, -1, -2]
dc = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(r, c):
    global er, ec
    dq = deque([(r, c, 0)])
    visited[r][c] = True

    while dq:
        cr, cc, count = dq.popleft()
        # 도착했는지 확인
        if cr == er and cc == ec:
            return count

        # 8개 방향 탐색
        for i in range(8):
            nr = cr + dr[i]
            nc = cc + dc[i]
            # range는 시간이 많이 걸린다.
            # if nr in range(L) and nc in range(L) and not visited[nr][nc]:
            if 0 <= nr < L and 0 <= nc < L and not visited[nr][nc]:
                if cr == er and cc == ec:
                    return count
                dq.append((nr, nc, count + 1))
                visited[nr][nc] = True


TC = int(input())
for tc in range(TC):
    L = int(input())
    sr, sc = list(map(int, input().split()))
    er, ec = map(int, input().split())
    visited = [[False] * L for _ in range(L)]
    answer = bfs(sr, sc)
    print(answer)