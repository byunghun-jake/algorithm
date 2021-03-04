import sys

sys.stdin = open("input.txt")
N = 100

for _ in range(10):
    # 1. test_case 번호 입력
    tc = int(input())

    # 2. 100x100 배열 입력
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    # 3. [99, 0] 부터 오른쪽으로 이동하며, 2의 위치 찾기
    r = N - 1
    c = 0
    for c_idx in range(N):
        if arr[r][c_idx] == 2:
            c = c_idx
            break
    
    # 4. 도착점부터 위로 올라가며, 작업 수행
    while r > 0:
        # 4-1. 좌우를 탐색하며 1을 찾는다.
        dc = 0
        nc = 0

        # 왼쪽 확인
        if 0 <= c-1 and arr[r][c-1] == 1:
            dc = -1
        elif c+1 < 100 and arr[r][c+1] == 1:
            dc = 1

        if dc:
            nc = c + dc
            while 0 <= nc < 100 and arr[r][nc] == 1:
                nc += dc
            else:
                nc -= dc
                c = nc
        r -= 1
        if r == 0:
            break
    result = c

    print(f"#{tc} {result}")


























