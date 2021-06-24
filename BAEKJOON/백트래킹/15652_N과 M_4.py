# 1부터 N까지 자연수 중에서 M개를 고른 수열
# 같은 수를 여러번 골라도 된다.
# 고른 수열은 비내림차순이어야 한다. (이전 값보다 크거나 같아야 한다.)

# 선택한 숫자를 저장하는 배열: sel
# 어떤 숫자를 선택했는지 저장하는 배열은 없어도 된다.
# 함수 내에 반복문을 통해 값을 하나씩 넣어본다.

import sys

N, M = map(int, sys.stdin.readline().strip().split())

sel = [0] * M

def permutation(idx):
    if idx == M:
        print(*sel)
        return

    # 1부터 N까지
    for i in range(1, N + 1):
        if idx != 0 and i < sel[idx - 1]:
            continue
        else:
            sel[idx] = i
            permutation(idx + 1)

permutation(0)