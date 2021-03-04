import sys

sys.stdin = open("input.txt")

# NxN 크기의 미로에서 출발지 목적지가 주어진다
# 도착지에 도달하는 최소 거리를 구하시오
# 경로가 없는 경우 0을 출력한다
# 1은 벽
# 0은 통로
# 출발지: 2
# 도착지: 3

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(sr, sc):
    # queue: 방문할 좌표를 저장
    queue = [(sr, sc)]
    # 시작지점은 방문으로 표시, 거리는 0
    visited[sr][sc] = 0

    while queue:
        r, c = queue.pop(0)
        # 사방 탐색
        for idx in range(len(dr)):
            nr = r + dr[idx]
            nc = c + dc[idx]
            # 탐색할 위치가 미로를 벗어나면 안된다.
            if -1 < nr < N and -1 < nc < N:
                # 벽이거나 방문했던 지점이라면, 탐색 종료
                if MAZE[nr][nc] == 1 or visited[nr][nc] != -1:
                    continue
                # 도착지점이면 탐색 종료
                if MAZE[nr][nc] == 3:
                    # 기준 정점(r,c)의 거리를 리턴한다 (지나온 통로의 개수이므로)
                    return visited[r][c]
                # 통로라면, 탐색을 이어간다.
                visited[nr][nc] = visited[r][c] + 1
                queue.append((nr, nc))
    else:
        return 0

TC = int(input())
for tc in range(1, TC + 1):
    # N: 미로의 크기
    N = int(input())

    # MAZE: 미로
    MAZE = [list(map(int, input())) for _ in range(N)]

    # 출발 지점을 찾습니다
    starting_node = None
    for i in range(N):
        for j in range(N):
            if MAZE[i][j] == 2:
                starting_node = (i, j)
        if starting_node:
            break

    # 미로를 탐색해볼까요?
    # visited: 방문 여부 확인 및 방문 시 거리를 값으로 변경
    visited = [[-1] * N for _ in range(N)]
    result = bfs(starting_node[0], starting_node[1])

    print(f"#{tc} {result}")




