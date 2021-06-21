# 자연수 N과 M이 주어졌을 때
# 1부터 N까지의 자연수 중에서 중복 없이 M개를 고른 수열
# 사전 순으로 증가하는 순서로 출력
# M = 8
# N = 8
# 시간 제한: 1초

# 작은 숫자부터 선택 & 선택하지 않음 순서로 진행

import sys

N, M = map(int, sys.stdin.readline().strip().split())

# sel: 선택한 값을 저장하는 배열
# M개의 수를 뽑을 것이므로 길이는 M
sel = [0] * M
# check: 어떤 값을 선택했는지 저장하는 배열
# 1 ~ N까지의 수를 관리해야 하기에 길이는 N + 1
check = [0] * (N + 1)


# def permutation(idx):
#     if idx == M:
#         print(*sel)
#         return
#     for i in range(1, N + 1):
#         if check[i] == 0:
#             sel[idx] = i
#             check[i] = 1
#             permutation(idx + 1)
#             check[i] = 0

def permutation(idx):
    # idx: 선택한 숫자의 개수이자, sel에 값을 넣을 인덱스
    if idx == M:
        print(*sel)
        return

    for i in range(1, N + 1):
        if i in sel:
            continue
        sel[idx] = i
        permutation(idx + 1)
        sel[idx] = 0


permutation(0)