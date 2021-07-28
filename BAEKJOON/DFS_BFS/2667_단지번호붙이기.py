# 1. 1의 값을 찾는 과정
# 2. 1을 찾았을 때, 해당 지점을 방문한 적이 있었는지 확인
# 3. 방문한 적이 있었다면 넘어간다.
# 4. 방문한 적이 없었다면 그 위치를 기준으로 4방향으로 탐색을 진행한다.
# 5. 탐색이 끝났다면 단지의 크기를 저장한다.
# 6. 단지 인덱스를 1 크게 해준 뒤, 다시 1번으로 돌아간다.

# N: 지도의 크기 (~25)
N = int(input())
MAP = [list(map(int, list(input()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(sr, sc):
    count = 1
    queue = [(sr, sc)]
    visited[sr][sc] = True

    while queue:
        snr, snc = queue[0]
        for i in range(4):
            nnr = snr + dr[i]
            nnc = snc + dc[i]
            if 0 <= nnr < N and 0 <= nnc < N:
                if MAP[nnr][nnc] and not visited[nnr][nnc]:
                    queue.append((nnr, nnc))
                    count += 1
                    visited[nnr][nnc] = True
        else:
            queue.pop(0)
    return count


count_list = []

for r in range(N):
    for c in range(N):
        if MAP[r][c] and not visited[r][c]:
            count_list.append(bfs(r, c))

print(len(count_list))
for count in sorted(count_list):
    print(count)

###############