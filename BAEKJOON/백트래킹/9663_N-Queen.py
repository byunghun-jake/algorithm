# 퀸 N개를 서로 공격할 수 없게 놓는 문제
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램

# 퀸을 놓기 전 조건
# 1. 같은 행에는 놓을 수 없다. (r)
# 2. 같은 열에는 놓을 수 없다. (c)
# 3. 좌상우하 대각선에는 놓을 수 없다. (r - c)
# 4. 좌하우상 대각선에는 놓을 수 없다. (r + c)

N = int(input())
BOARD = [[0] * N for _ in range(N)]
result = 0
check_r = [0] * N
check_c = [0] * N
check_d1 = [0] * (2 * N - 1)
check_d2 = [0] * (2 * N - 1)
# [0, 1, 2, -2, -1]

def queen(sr, count):
    global result
    # 종료 조건
    if sr == N:
        result += 1
        return

    for j in range(N):
        # 같은 열, 대각선에 있는 경우
        if check_c[j] or check_d1[sr - j] or check_d2[sr + j]:
            continue
        # 말을 놓음
        check_c[j] = 1
        check_d1[sr - j] = 1
        check_d2[sr + j] = 1
        queen(sr + 1, count + 1)
        # 말을 치움
        check_c[j] = 0
        check_d1[sr - j] = 0
        check_d2[sr + j] = 0



queen(0, 0)
print(result)
