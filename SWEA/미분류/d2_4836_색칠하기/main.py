import sys

sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    # 색칠 횟수 입력
    c_count = int(input())
    # 10x10 배열 초기화
    palette = [[0]*10 for _ in range(10)]
    # print(palette)

    # 색칠 횟수만큼 반복문을 수행하고, 빨간색은 1을 파란색은 2를 값에 넣는다.
    for _ in range(c_count):
        r1, c1, r2, c2, color = map(int, input().split())

        # 반복문을 이용해 해당 영역을 색칠한다.
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                # 이미 색이 칠해져 있는 경우
                if palette[i][j] == color or palette[i][j] == 3:
                    continue
                # 색이 칠해지지 않은 경우
                palette[i][j] += color

    # 배열을 순회하며 3을 찾는다.
    count = 0
    for r in range(10):
        for c in range(10):
            if palette[r][c] == 3:
                count += 1

    print(f"#{tc} {count}")





























