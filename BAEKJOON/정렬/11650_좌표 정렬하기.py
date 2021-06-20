# 시간제한 1초
# N = 100,000
# 2가지를 기준으로 정렬하기
    # 1. y좌표
    # 2. x좌표

import sys

N = int(sys.stdin.readline().strip())
NODES = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
# print(NODES)

# sort 사용하기
# NODES.sort(key=lambda node: node[1])
# NODES.sort(key=lambda node: node[0])

# 병합정렬
def merge(left, right):
    # 합칠 값을 저장할 배열 선언
    result = []

    # 양쪽 배열의 현재 진행중인 인덱스를 저장
    left_index, right_index = 0, 0

    # 양쪽 배열 중 하나라도 끝날 때까지 반복한다.
    while len(left) > left_index and len(right) > right_index:
        # 두 배열의 현재 인덱스 값을 비교한다.
        # 값을 비교할 때, 해당 인덱스에 있는 값을 비교해야 한다.
        # x값을 비교한다.
        if left[left_index][0] == right[right_index][0]:
            # x좌표가 같다면, y좌표를 비교한다.
            if left[left_index][1] < right[right_index][1]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        elif left[left_index][0] < right[right_index][0]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    # 남은 배열을 더해준다.
    if len(left) != left_index:
        result += left[left_index:]
    else:
        result += right[right_index:]

    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    # 정렬을 반으로 나눈다.
    mid = len(arr) // 2
    # 나눈 값들을 다시 나누어준다.
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    # 양쪽을 다 나눈 후에 여기로 돌아왔다면, 그 둘을 합쳐준다.
    return merge(left, right)

sorted_NODES = mergeSort(NODES)

# print(NODES)
for i in range(N):
    print(*sorted_NODES[i])