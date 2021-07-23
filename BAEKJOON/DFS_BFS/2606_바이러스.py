from collections import deque

# 시작 정점(1)과 연결된 정점의 개수를 출력하시오 (시작 정점 제외)

# N: 컴퓨터의 수 (~100)
N = int(input())

# M: 연결의 수
M = int(input())

node_map = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    N1, N2 = map(int, input().split())
    node_map[N1][N2] = node_map[N2][N1] = True


visited = [False] * (N + 1)
visited[1] = True
answer = 0

# stack = [1]
# while stack:
#     s = stack[-1]
#
#     for e in range(1, N + 1):
#         if node_map[s][e] and not visited[e]:
#             visited[e] = True
#             answer += 1
#             stack.append(e)
#             break
#     else:
#         stack.pop()


queue = deque([1])
while queue:
    s = queue.popleft()

    for e in range(1, N + 1):
        if node_map[s][e] and not visited[e]:
            queue.append(e)
            visited[e] = True
            answer += 1

print(answer)