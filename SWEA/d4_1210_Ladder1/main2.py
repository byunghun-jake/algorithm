import sys

sys.stdin = open("input.txt")

N = 100
for _ in range(10):
    tc = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    
    # Find EndPoint
    cr = N-1
    cc = 0
    for c in range(N):
        if arr[cr][c] == 2:
            cc = c
            break
    
    # direction 상(0), 좌(1), 우(2)
    delta = [(-1, 0), (0, -1), (0, 1)]
    direction = 0
    
    # current_row가 0이 될 때까지 반복
    while cr > 0:
        # 방향 탐색 (i: 탐색 방향)
        for i in range(3):
            # 진행방향(direction)과 탐색방향(i)이 일치하는 경우는 탐색 대상이 아니며,
            # 왼쪽으로 이동중에 오른쪽을 탐색하지는 않는다 (i*direction != 0)
            if direction == i or i * direction != 0:
                continue

            nr = cr + delta[i][0]
            nc = cc + delta[i][1]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 1:
                direction = i
                break

        # 방향으로 진행
        cr += delta[direction][0]
        cc += delta[direction][1]

    print(f"#{tc} {cc}")




































