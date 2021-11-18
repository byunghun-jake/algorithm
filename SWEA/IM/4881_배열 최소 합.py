def solve(arr):
    global min_sum
    if len(arr) == N:
        if min_sum > sum(arr):
            min_sum = sum(arr)
            print(arr)
        return

    for c in range(N):
        if visited_c[c]:
            continue
        visited_c[c] = True
        solve(arr + [board[len(arr)][c]])
        visited_c[c] = False

T = int(input())

for _ in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited_c = [False] * N
    min_sum = 987654321
    solve([])
    print(min_sum)

