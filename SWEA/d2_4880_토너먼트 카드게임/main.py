# 1. 그룹을 반으로 나눈다
# 2. 그룹의 크기가 1이 되었다면, 스택에 넣는다
import sys

sys.stdin = open("input.txt")


def compare(compare_arr):
    a = compare_arr[0][0]
    b = compare_arr[1][0]
    if (a - b) == -1 or (a - b) == 2:
        return 1
    else:
        return 0


def solve(arr, idx_arr):
    # 종료 조건
    if len(arr) == 1:
        return arr[0], idx_arr[0]

    # 배열을 반으로 나눈다.
    mid_idx = (len(arr) // 2) + (len(arr) % 2)

    a_arr = arr[:mid_idx]
    a_idx_arr = idx_arr[:mid_idx]
    b_arr = arr[mid_idx:]
    b_idx_arr = idx_arr[mid_idx:]

    # 비교
    temp = [solve(a_arr, a_idx_arr), solve(b_arr, b_idx_arr)]
    idx = compare(temp)
    return temp[idx][0], temp[idx][1]


TC = int(input())
for tc in range(1, TC+1):
    # N: 인원수
    N = int(input())

    # rsp_list: 가위바위보 리스트
    rsp_list = list(map(int, input().split()))
    # index_list: index를 보관하고 있는 리스트
    index_list = [i for i in range(1, N+1)]

    result = solve(rsp_list, index_list)
    print(f"#{tc} {result[1]}")