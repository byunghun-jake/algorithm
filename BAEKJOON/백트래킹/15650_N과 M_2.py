# 자연수 N과 M이 주어졌을 때

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
    # if idx == M:
        # print(sel)
        # return

# 고른 수열은 오름차순이어야 한다.
    # for i in range(1, N + 1):
        # if idx != 0 and i < sel[idx - 1]:
            # continue


import sys

N, M = map(int, sys.stdin.readline().strip().split())

# 선택한 M개의 수를 저장하는 배열
sel = [0] * M
# 선택 받은 수라는 것을 저장하는 배열
check = [0] * (N + 1)

def permutation(idx):
    if idx == M:
        print(*sel)
        return

    for i in range(1, N + 1):
        if check[i] == 1:
            continue
        if idx != 0 and i < sel[idx - 1]:
            continue
        # 숫자 선택
        check[i] = 1
        sel[idx] = i
        # 다음 단계로
        permutation(idx + 1)
        # 돌아왔다면, 선택한 숫자는 취소
        check[i] = 0

permutation(0)