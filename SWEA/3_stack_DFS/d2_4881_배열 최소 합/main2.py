import sys

sys.stdin = open("input.txt")


# 종료 조건: row_idx == N
def dfs(idx, total):
    global min_total

    # 만약, total이 min_total보다 크다면 이 방향으로 더 진행할 필요가 없다.
    if min_total < total:
        return

    # 종료 조건
    if idx == N:
        # 지금까지 더한 값과 최소 합을 비교한다.
        if min_total > total:
            min_total = total
        return

    # 유망성 탐색
    # 현재 row에서 갈 수 있는 column을 찾는다
    for c in range(N):
        if not visited[c]:
            visited[c] = True                   # 현재 위치 방문도장 찍기
            next_total = total + arr[idx][c]    # 현재 위치 값 더함
            dfs(idx+1, next_total)              # 다음 row에 대해 탐색
            visited[c] = False                  # 돌아온 후 방문도장 지우기


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N

    min_total = 10 * N
    dfs(0, 0)

    print(f"#{tc} {min_total}")