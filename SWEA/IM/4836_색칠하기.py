# 격자를 준비한다 (0으로 초기화한다)
# 빨간색을 칠한다 (0 또는 2이면 칠한다, +1)
# 파란색을 칠한다 (0 또는 1이면 칠한다, +2)
# 보라색을 찾는다 (3의 값을 갖는 칸을 찾는다)

# 빨간색과 파란색의 왼쪽 위 인덱스 각각 최소 값을 찾아 새로운 인덱스로 만든다
# 빨간색과 파란색의 오른쪽 아래 인덱스 각각 최대 값을 찾아 새로운 인덱스로 만든다

T = int(input())

for _ in range(T):
    # N: 칠할 영역의 개수
    N = int(input())
    paper = [[0] * 10 for _ in range(10)]
    count = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if paper[r][c] == color or paper[r][c] == 3:
                    continue
                else:
                    paper[r][c] += color
                    if paper[r][c] == 3:
                        count += 1
    print(count)