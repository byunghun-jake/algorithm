# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# N의 최대가 1000이다. O(n^2)까지 가능하다.

# 정렬 방식
    # 1. 선택 정렬
    # 2.

import sys
sys.setrecursionlimit(1000000)

def selectionSort_recursion(current_idx):
    if current_idx == N:
        return

    min_num = ARR[current_idx]
    min_idx = current_idx
    for i in range(current_idx, N):
        if min_num > ARR[i]:
            min_idx = i
            min_num = ARR[i]
    else:
        ARR[current_idx], ARR[min_idx] = ARR[min_idx], ARR[current_idx]
    selectionSort_recursion(current_idx + 1)


def selectionSort_loop():
    for c_idx in range(N):
        min_idx = c_idx
        for target_idx in range(c_idx + 1, N):
            if ARR[min_idx] > ARR[target_idx]:
                min_idx = target_idx
        else:
            ARR[c_idx], ARR[min_idx] = ARR[min_idx], ARR[c_idx]


# N: 수의 개수
# ARR: 수가 담긴 배열
N = int(input())
ARR = [int(input()) for _ in range(N)]

# 정렬
# 1. 선택정렬
# selectionSort_recursion(0)
selectionSort_loop()
for i in range(N):
    print(ARR[i])
