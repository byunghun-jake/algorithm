# 좌표 정렬하기 문제와 동일
# 시간 제한 1초
# 메모리 제한 256MB
# N = 100,000

# 정렬 순서
    # 1. x좌표 기준
    # 2. y좌표 기준
    # => 결과적으로는 y좌표 기준으로 정렬이 되지만, 서브 정렬 기준은 x좌표인 것

import sys

N = int(sys.stdin.readline().strip())
NODES = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

def merge(left, right):
    result = []

    l_idx, r_idx = 0, 0
    L = len(left)
    R = len(right)
    while L > l_idx and R > r_idx:
        if left[l_idx][1] == right[r_idx][1]:
            if left[l_idx][0] < right[r_idx][0]:
                result.append(left[l_idx])
                l_idx += 1
            else:
                result.append(right[r_idx])
                r_idx += 1
        elif left[l_idx][1] < right[r_idx][1]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1

    if L != l_idx:
        result += left[l_idx:]
    else:
        result += right[r_idx:]

    return result

def mergeSort(arr):
    # 길이가 1이하인 경우에는 그 값을 그대로 반환한다.
    if len(arr) <= 1:
        return arr

    # 배열을 반으로 나눈 뒤, 다시 나누기 위해 mergeSort를 호출한다.
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    # 여기로 돌아온 배열들은 합쳐준다.
    return merge(left, right)


sortedNodes = mergeSort(NODES)

for i in range(N):
    print(*sortedNodes[i])