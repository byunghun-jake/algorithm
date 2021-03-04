import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # N: 퍼즐 크기
    # M: 단어 길이
    N, M = map(int, input().split())

    # arr: 행렬
    arr = [list(map(int, input().split())) for _ in range(N)]

    # result: 자리 수
    result = 0

    for r in range(N):
        count = 0
        c = 0
        while c < N:
            if arr[r][c] == 0 or c == N-1:
                if count == M:
                    result += 1
                count = 0
            else:
                count += 1

            c += 1

        # for c in range(N):
        #     마지막이 1로 끝나고, 그 결과 M칸이 완성되는 경우
        #     if arr[r][c] == 0 or c == N-1:
        #         if count == M:
        #             result += 1
        #         count = 0
        #     else:
        #         count += 1
        #

    for c in range(N):
        count = 0
        for r in range(N):
            if arr[r][c] == 0:
                if count == M:
                    result += 1
                count = 0
            else:
                count += 1
        else:
            if count == M:
                result += 1

    print(result)










































