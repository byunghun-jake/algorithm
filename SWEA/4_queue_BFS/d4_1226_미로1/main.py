import sys

sys.stdin = open("input.txt")

# 10개의 테스트케이스
# 16x16 크기의 미로
# 출발점은 (1, 1)로 고정
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs():
    sr = 1
    sc = 1
    # 시작지점을 방문하였습니다.
    visited[sr][sc] = True
    # 시작지점부터 탐색할 것이기에 queue에 좌표를 넣어줍니다.
    queue = [(sr, sc)]

    while queue:
        # 현재 정점의 좌표를 꺼냅니다.
        cr, cc = queue.pop(0)

        # 갈 수 있는 좌표를 탐색합니다.
        for idx in range(4):
            nr = cr + dr[idx]
            nc = cc + dc[idx]
            # 벽으로 감싸져있기 때문에, 인덱스 검사는 생략합니다.
            # 갈 수 있는 조건: 벽이 아니고, 간 적이 없음
            if MAZE[nr][nc] != 1 and not visited[nr][nc]:
                # 갈 수 있는 좌표는 queue에 추가합니다.
                queue.append((nr, nc))
                # queue에 넣음으로써 방문이 확실해졌기 때문에,
                # visited에도 해당 좌표에 방문했음을 미리 저장합니다.
                visited[nr][nc] = True
                # 갈 수 있는 좌표가 도착지점이라면, 탐색을 종료합니다.
                if MAZE[nr][nc] == 3:
                    return 1
    # 갈 수 있는 모든 경로를 탐색했지만, 도착지점을 찾을 수 없었어요.
    else:
        return 0



for _ in range(10):
    tc = int(input())
    MAZE = [list(map(int, input())) for _ in range(16)]

    # 미로 탐색 시작
    visited = [[False] * 16 for _ in range(16)]
    result = bfs()
    print(f"#{tc} {result}")