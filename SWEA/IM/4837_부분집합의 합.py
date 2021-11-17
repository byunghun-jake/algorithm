T = int(input())

def solve(_arr):
    global answer
    if len(_arr) == N:
        if sum(_arr) == K:
            answer += 1
        return

    for n in range(_arr[-1] + 1, 13):
        solve(_arr + [n])

for _ in range(T):
    # N: 원소의 개수
    # K: 원소의 합
    N, K = map(int, input().split())
    answer = 0
    for i in range(1, 13):
        solve([i])
    print(answer)