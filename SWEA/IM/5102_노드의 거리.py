from collections import deque

def bfs(s):
    dq = deque([[s, 0]])
    visited = [False] * (V + 1)
    visited[s] = True

    while dq:
        c_node, count = dq.popleft()
        # 갈 수 있는 곳 탐색
        for n_node in range(1, V + 1):
            if not adj_matrix[c_node][n_node] or visited[n_node]:
                continue
            if n_node == G:
                return count + 1
            dq.append([n_node, count + 1])
            visited[n_node] = True
    return 0

T = int(input())

for _ in range(T):
    # V: 노드의 개수 (노드 번호는 1번부터)
    # E: 간선의 개수
    V, E = map(int, input().split())
    adj_matrix = [[False] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        N1, N2 = map(int, input().split())
        adj_matrix[N1][N2] = True
        adj_matrix[N2][N1] = True

    S, G = map(int, input().split())

    answer = bfs(S)
    print(answer)