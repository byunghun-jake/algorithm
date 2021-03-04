import sys

sys.stdin = open("input.txt")


def dfs(S, G):
    stack = list()
    visited = [0] * (V + 1)
    # 시작 정점 방문처리
    stack.append(S)
    visited[S] = 1
    while stack:
        current_node = stack.pop()
        for i in range(1, V+1):
            if adj[current_node][i] == 1 and visited[i] != 1:
                if i == G:
                    return 1
                stack.append(i)
                # visited[i] = 1
    return 0





def dfs2(n):
    visited2[n] = 1
    if n == G:
        return 1

    for i in range(1, V+1):
        if adj[n][i] and visited2[i] != 1:
            if dfs2(i) == 1:
                return 1

    return 0

TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        s, e = map(int, input().split())
        # 그래프의 모양(간선)은 인접행렬로 표현된다
        adj[s][e] = 1

    S, G = map(int, input().split())
    # result = dfs(S, G)
    visited2 = [0] * (V+1)
    result2 = dfs2(S)
    print(result2)
