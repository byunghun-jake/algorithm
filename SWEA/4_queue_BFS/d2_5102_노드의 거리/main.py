import sys

sys.stdin = open("input.txt")


def bfs():
    # S: 출발 노드
    # G: 도착 노드
    visited[S] = 0
    queue = [S]

    while queue:
        front = queue.pop(0)
        # 갈 수 있는 경로 확인
        for c in range(V + 1):
            # 갈 수 있고, 방문한 적이 없다면
            if adj[front][c] != 0 and visited[c] == -1:
                # 도착지점인지 확인
                if c == G:
                    return visited[front] + 1
                # 도착지점이 아니라면, 탐색을 이어나갈 수 있도록
                queue.append(c)
                visited[c] = visited[front] + 1
    # while문을 도는 동안 도착지점을 찾지 못했다면,
    else:
        return 0


# 간선의 방향성은 없음
TC = int(input())
for tc in range(1, TC + 1):
    # V: 노드의 개수
    # E: 간선의 개수
    V, E = map(int, input().split())

    adj = [[0] * (V + 1) for _ in range(V + 1)]

    # 간선 정보 입력받기
    for _ in range(E):
        n1, n2 = map(int, input().split())
        # print(n1, n2)
        adj[n1][n2] = 1
        adj[n2][n1] = 1
    # print(adj)
    
    # 출발 노드 S / 도착 노드 G
    S, G = map(int, input().split())

    # 그래프 탐색
    # visited 방문 확인 및 거리 확인
    visited = [-1] * (V + 1)
    result = bfs()
    print(f"#{tc} {result}")