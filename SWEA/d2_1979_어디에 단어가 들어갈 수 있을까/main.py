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
    
    # 행 우선 순환 / 열 우선 순환
    # 1로 시작하거나 0을 만난 뒤 1이 나타났을 때, 1이 나타난 갯수를 세어 M과 일치하면 카운트
    for r in range(N):
        for s in range(0, N-M+1):
            # 시작지점 바로 전 인덱스가 0 미만 또는 값이 0인 경우
            if s == 0 or arr[r][s-1] == 0:
                # 탐색 시작
                for c in range(M):
                    # 0을 만났을 때,
                    if arr[r][s+c] == 0:
                        break
                else:
                    # 다음 자리가 1일 때,
                    if s+M < N and arr[r][s+M]:
                        continue
                    result += 1

    for c in range(N):
        for s in range(0, N - M + 1):
            # 시작지점 바로 전 인덱스가 0 미만 또는 값이 0인 경우
            if s == 0 or arr[s - 1][c] == 0:
                # 탐색 시작
                for r in range(M):
                    # 0을 만났을 때,
                    if arr[s + r][c] == 0:
                        break
                else:
                    # 다음 자리가 1일 때,
                    if s + M < N and arr[s + M][c]:
                        continue
                    result += 1

    print(f"#{tc} {result}")


































