import sys

sys.stdin = open("input.txt")

N = 100

for _ in range(1, 11):
    tc = int(input())

    # arr: 문자열
    arr = [list(input()) for _ in range(N)]

    start = 0
    end = N-1
    # L: pelindrome의 최대 길이
    L = 1

    # 회문을 좀 더 빠르게 찾아내는 방법은 없을까?
    # 회문의 내부도 회문이기 때문에, 중간부터 문자열을 만들어나가는 건 어떨까?
    for c in range(N):
        for s in range(N-1):
            for e in range(N-1, s, -1):
                if (e-s) < L:
                    break
                start = s
                end = e
                while start < end:
                    # 회문이 아닐 때,
                    if arr[start][c] != arr[end][c]:
                        break
                    start += 1
                    end -= 1
                # 회문일 때,
                else:
                    L = e-s+1

    for r in range(N):
        for s in range(N-1):
            for e in range(N-1, s, -1):
                if (e-s) < L:
                    break
                start = s
                end = e
                while start < end:
                    if arr[r][start] != arr[r][end]:
                        break
                    start += 1
                    end -= 1
                else:
                    L = e-s+1

    print(f"#{tc} {L}")


































