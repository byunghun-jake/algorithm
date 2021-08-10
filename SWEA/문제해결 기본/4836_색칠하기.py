# 왼쪽 위와 오른쪽 아래 인덱스가 주어진다.
# 오른쪽 아래 인덱스를 포함하여 색칠하는 것에 대해 주의하자!
# 기본 값을 0으로 설정해 두고, 색칠하며 해당 영역에 숫자를 더하는 식으로 진행한 뒤
# 전체 배열을 순회하여, 3인 값을 찾아보자.

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    paper = [[0] * 10 for _ in range(10)]
    answer = 0
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                paper[r][c] += color
                if paper[r][c] == 3:
                    answer += 1

    print(f"#{tc} {answer}")
