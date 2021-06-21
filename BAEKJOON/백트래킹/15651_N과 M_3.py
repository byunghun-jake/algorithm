# 같은 숫자를 여러번 골라도 된다.
    # 같은 숫자를 고르지 못하게 했던 조건을 없앰
        # if check[i] == 1:
            # continue

import sys

N, M = map(int, sys.stdin.readline().strip().split())

# 뽑은 숫자를 저장하는 배열
sel = [0] * M
# 해당 숫자를 뽑았음을 저장하는 배열
check = [0] * (N + 1)

def permutation(idx):
    if idx == M:
        print(*sel)
        return

    for i in range(1, N + 1):
        # 선택
        check[i] = 1
        sel[idx] = i
        permutation(idx + 1)
        # 선택 취소
        check[i] = 0

permutation(0)