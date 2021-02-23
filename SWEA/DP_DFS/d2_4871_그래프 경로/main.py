# 방향성이 있는 그래프 경로
# 1. 간선 정보를 인접 행렬에 정리한다.
# 2. 출발 노드와 도착 노드를 입력받아, 순회 중에 만나는지 확인한다.
import sys

sys.stdin = open("input.txt")


def dfs1(v):
    """
    :param v:
    :return visited:
    """
    stack = []
    # 최대 노드의 인덱스 50
    visited = [False] * 51

    visited[v] = True
    stack.append(v)

    while len(stack):
        current_node = stack.pop()
        # 방문 도장 쾅
        visited[current_node] = True

        # 갈 수 있는 인접 노드 탐색
        for c in range(len(adj)):
            if adj[current_node][c] == 1 and not visited[c]:
                stack.append(c)
    return visited


def dfs2(v):
    # 방문 도장
    visited2[v] = True

    # 갈 수 있는 인접 노드 탐색
    for c in range(len(adj)):
        if adj[v][c] == 1 and not visited2[c]:
            dfs2(c)

# T: 테스트 케이스 개수
T = int(input())
for tc in range(1, T+1):
    # V: 노드 개수
    # E: 간선 개수
    V, E = map(int, input().split())

    # 인접 행렬 생성
    adj = [[0] * (V+1) for _ in range(V+1)]

    # 간선 정보를 인접 행렬에 저장
    for i in range(E):
        s, e = map(int, input().split())
        adj[s][e] = 1

    # S: 출발 노드
    # G: 도착 노드
    S, G = map(int, input().split())

    result = 0
    if dfs1(S)[G]:
        result = 1

    print(f"#{tc} {result}")

    ###########################################

    visited2 = [False] * (V+1)
    result2 = 0
    dfs2(S)
    if visited2[G]:
        result2 = 1
    print(f"#{tc} {result2}")






































